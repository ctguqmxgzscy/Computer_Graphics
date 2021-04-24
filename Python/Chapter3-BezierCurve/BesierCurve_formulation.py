import numpy as np
import matplotlib.pyplot as plt
import math

#-------------------------函数定义部分------------------------------
#获得顶点控制函数的定义，并画出控制顶点
def get_CtrlPoints(n):
    listX,listY=[],[]
    i=1
    while i<=n:
        print("请输入第",i,"个控制顶点的x,y坐标:")
        x,y=map(float,input().split())
        listX.append(x)
        listY.append(y)
        i+=1
    return np.array([listX,listY])
#斯特林-阶乘近似公式 ((2*PI*x)^1/2)*((x/e)^x) 
def Stirling(x): 
    if x==0:
        return 1.0;
    return math.pow(2*math.pi*x,0.5)*math.pow(x/math.e,x)
#伯恩施坦多项式 n!/(i!*(n-i)!)*t^i*(1-t)^(n-i)
def Bernstein(n,i,t):
    return Stirling(n)/(Stirling(i)*Stirling(n-i))*math.pow(t,i)*math.pow(1-t,n-i)
#绘制Bezier曲线函数定义(参数数组t[],控制顶点数组,阶数r,控制顶点数n)
def draw_BezierCurve(values_T,ctrlPts,r):
   #绘制部分
    xmin,xmax,ymin,ymax=0,800,0,800
    plt.axis([xmin,xmax,ymin,ymax])
    plt.axis("on")
    plt.scatter(ctrlPts[0],ctrlPts[1],color="r")
    #利用公式法直接求出P(t) P(t)= SUM(B(t)*Pi)
    list_x,list_y=[],[]
    for value_t in values_T:
        Pt_x,Pt_y=0,0
        for i in range(0,r+1):
            Pt_x+=Bernstein(r,i,value_t)*ctrlPts[:,i][0]
            Pt_y+=Bernstein(r,i,value_t)*ctrlPts[:,i][1]
        list_x.append(Pt_x)
        list_y.append(Pt_y)
    plt.plot(list_x,list_y)
    plt.show()
#-------------------------------------------------------------------
        
#----------------------主函数部分----------------------------
#定义贝塞尔曲线的阶数和控制顶点数
r=int(input("请输入贝塞尔曲线的阶数r:"))
n=r+1
print("当前贝塞尔曲线的阶数为:",r,"     控制顶点有:",n,"个")

#获得顶点控制数组
ctrlPts=get_CtrlPoints(n)

#获得参数t的最小单位长度和参数数组values_t
minL=float(input("请输入参数t的最小单位长度minL:"))
values_t=np.arange(0,1+minL,minL)

#使用de_casteliau绘制r阶贝塞尔曲线
draw_BezierCurve(values_t,ctrlPts,r) 
#------------------------------------------------------------

