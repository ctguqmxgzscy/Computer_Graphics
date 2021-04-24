import numpy as np
import matplotlib.pyplot as plt

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

#de kastliau函数定义(参数t,拷贝数组,阶数r,控制顶点数n)
def de_kastliau(value_t,copy_array,r,n):
    # r阶贝塞尔曲线需要循环r次才能得到唯一确定的顶点P(t)
    for i in range(1,r+1):
        # P(j)=(1-t)*P(j)+t*P(j+1)
        for j in range(0,n-i):
            copy_array[0,j]=(1-value_t)*copy_array[0,j]+value_t*copy_array[0,j+1]
            copy_array[1,j]=(1-value_t)*copy_array[1,j]+value_t*copy_array[1,j+1]
    #返回copy_array的第一列的横纵坐标[x,y]，即P(t)
    print(copy_array[:,0])
    return copy_array[:,0]

#绘制Bezier曲线函数定义(参数数组t[],控制顶点数组,阶数r,控制顶点数n)
def draw_BezierCurve(values_T,ctrlPts,r,n):
    ptsCopy=ctrlPts.copy()
    #创建list_xAxis和list_yAxis列表分别来接收P(t)的横纵坐标
    list_xAxis,list_yAxis=[],[]
    for value_t in values_T:
        temp=de_kastliau(value_t,ptsCopy,r,n)
        list_xAxis.append(temp[0])
        list_yAxis.append(temp[1])
    #绘制部分
    xmin,xmax,ymin,ymax=0,800,0,800
    plt.axis([xmin,xmax,ymin,ymax])
    plt.axis("on")
    plt.scatter(ctrlPts[0],ctrlPts[1],color="r")
    plt.plot(list_xAxis,list_yAxis)
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
draw_BezierCurve(values_t,ctrlPts,r,n)
#------------------------------------------------------------


