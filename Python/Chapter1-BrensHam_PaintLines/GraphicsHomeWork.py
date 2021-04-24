import numpy as np
import math
import matplotlib.pyplot as plt

xmin,xmax=(input("请输入栅格的大小<xmin,xmax>:").split())
xmin,xmax=int(xmin),int(xmax)
ymin,ymax=(input("请输入栅格的大小<ymin,ymax>:").split())
ymin,ymax=int(ymin),int(ymax)
print("栅格的x轴长度区间为： <",xmin,",",xmax,">")
print("栅格的x轴长度区间为： <",ymin,",",ymax,">")
plt.axis([xmin,xmax,ymin,ymax])
plt.axis('on')
plt.grid(True,color='blue')
deltax,deltay=1,1
plt.xticks(np.arange(xmin,xmax,deltax))
plt.yticks(np.arange(ymin,ymax,deltay))

#--------------------------------直线
#def drawLine(xplus,yplus,k,x0,y0,drawMode):
#    print("xplus:",xplus,"yplus:",yplus)
#    if(drawMode==1):#0<k<1
#        x,y=1,0.5
#        d=y-k*x
#        plt.scatter(0+x0,0+y0,color='r')
#        while x<xplus+1:
#            if(d>=0):   
#                plt.scatter(x+x0,y-0.5+y0,color='r')
#                d=d-k
#            else:      
#                plt.scatter(x+x0,y+0.5+y0,color='r')
#                d=d-k+1
#                y+=1
#            x+=1
#            #d=y-k*x
#    else:
#        if(drawMode==2):#k>1    
#             y,x=1,0.5
#             d=x-1/k*y
#             plt.scatter(0+x0,0+y0,color='r')
#             while y<yplus+1:    
#                if(d>=0):
#                    plt.scatter(x-0.5+x0,y+y0,color='r')
#                    d=d-1/k
#                else:      
#                    plt.scatter(x+0.5+x0,y+y0,color='r')
#                    d=d-1/k+1
#                    x+=1
#                y+=1
#                print(d)
#                #d=y-k*x  
#        else:
#            if(drawMode==3):#-1<k<0
#                  x,y=1,0.5
#                  d=y+k*x
#                  plt.scatter(0+x0,0+y0,color='r')
#                  while x<-xplus+1:
#                      if(d>=0):
#                            plt.scatter(-x+x0,y-0.5+y0,color='r')
#                            d=d+k
#                      else:      
#                            plt.scatter(-x+x0,y+0.5+y0,color='r')
#                            d=d+k+1
#                            y+=1
#                      x+=1
#            else: #k>-1
#                y,x=1,0.5
#                d=x+1/k*y
#                plt.scatter(0+x0,0+y0,color='r')
#                while y<yplus+1:
#                    if(d>=0):
#                        plt.scatter(-(x-0.5)+x0,y+y0,color='r')
#                        d=d+1/k
#                    else:      
#                        plt.scatter(-(x+0.5)+x0,y+y0,color='r')
#                        d=d+1/k+1
#                        x+=1
#                    y+=1
        
#x0,y0=(input("请输入线段的第一个点的横坐标和纵坐标：").split())
#x0,y0=float(x0),float(y0)
#x1,y1=(input("请输入线段的第二个点的横坐标和纵坐标：").split())
#x1,y1=float(x1),float(y1)

##使y坐标更高的点成为第二个点,确定该直线绘制模式
#drawMode=0
#if(y0>y1):
#        temp=y0
#        y0=y1
#        y1=temp
#        temp=x0
#        x0=x1
#        x1=temp
#xplus,yplus=x1-x0,y1-y0
#if(yplus==0):
#    x,y=0,0
#    plt.scatter(x+x0,y+y0,color='r');
#    print(drawMode,"----",xplus)
#    while xplus!=0 :
#        plt.scatter(x+1+x0,y+y0,color='r')
#        x=x+1
#        xplus=xplus-1
#else:
#    if(xplus==0):
#        x,y=0,0
#        print(drawMode,"----",yplus)
#        plt.scatter(x+x0,y+y0,color='r');
#        while yplus!=0 :
#            plt.scatter(x+x0,y+1+y0,color='r')
#            y=y+1
#            yplus=yplus-1 
#    else:
#        k=yplus/xplus
#        if(xplus>0):    #0<k<1
#            if(k<=1):
#                drawMode=1
#            else:       #k>1
#                drawMode=2
#        else:
#            if(k>-1):   #-1<k<0
#                drawMode=3
#            else:       #k>-1
#                drawMode=4
#            print("第一个点坐标：<",x0,",",y0,">")
#            print("第二个点坐标：<",x1,",",y1,">")
#            print("斜率k:",k)
#            print("画线模式：",drawMode)
#            if(drawLine!=0):
#                drawLine(xplus,yplus,k,x0,y0,drawMode)
#--------------------------------直线

#------------------------------------圆
x0,y0,r=(input("请输入圆的圆心坐标和半径长度：").split())
x0=float(x0)
y0=float(y0)
r=float(r)

def drawSymmetric(x,y,k):
    if(k==0):
        plt.scatter(x+x0,y+y0,color='r')
        plt.scatter(y+x0,x+y0,color='r')
        plt.scatter(-y+x0,-x+y0,color='r')
        plt.scatter(-x+x0,-y+y0,color='r')
    else :
        if(k==1):
            plt.scatter(x+x0,y+y0,color='r')
            plt.scatter(-x+x0,y+y0,color='r')
            plt.scatter(x+x0,-y+y0,color='r')
            plt.scatter(-x+x0,-y+y0,color='r')
        else:
            plt.scatter(x+x0,y+y0,color='r')
            plt.scatter(y+x0,x+y0,color='r')
            plt.scatter(-x+x0,-y+y0,color='r')
            plt.scatter(-y+x0,-x+y0,color='r')
            plt.scatter(-x+x0,y+y0,color='r')
            plt.scatter(-y+x0,x+y0,color='r')
            plt.scatter(x+x0,-y+y0,color='r')
            plt.scatter(y+x0,-x+y0,color='r')

x,y=0,r
d=math.pow(x+1,2)+math.pow(y-0.5,2)-math.pow(r,2)
drawSymmetric(0,r,0)
print("X:",x,"Y:",y,"Radius:",r)

while x<=y:
    print(d)
    
    if(d<0):
        drawSymmetric(x+1,y,(y)/(x+1))
        d=d+2*x+3
    else:
        drawSymmetric(x+1,y-1,y-1/(x+1))
        d=d+2*x+3-2*y+2
        y-=1
    x+=1
#------------------------------------圆
plt.show()