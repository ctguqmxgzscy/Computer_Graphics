import math
import matplotlib.pylab as plt
plt.axis([-100,100,-100,100])
plt.axis('on')
plt.xticks(np.arange(-100,100,10))
plt.yticks(np.arange(-100,100,10))
plt.grid(True)

x1,y1=(input("请输入第一个顶点的x,y坐标：").split())
v1=np.array([float(x1),float(y1),1])
x2,y2=(input("请输入第二个顶点的x,y坐标：").split())
v2=np.array([float(x2),float(y2),1])
x3,y3=(input("请输入第三个顶点的x,y坐标：").split())
v3=np.array([float(x3),float(y3),1])

print("第一个顶点的齐次坐标为：",v1)
print("第二个顶点的齐次坐标为：",v2)
print("第三个顶点的齐次坐标为：",v3)

triangle=np.array([v1,v2,v3])
triangle=np.vstack((triangle,v1))
gx,gy=(v1[0]+v2[0]+v3[0])/3.0,(v1[1]+v2[1]+v3[1])/3.0
print("三角形重心坐标为：<",gx,",",gy,">")
#[m,n]代表数据段集合中第m段数据的第n个分量，在矩阵里面就是第m个行向量的第n个分量
#[:,n]则是表示取所有行向量的第n个分量组成的数组 相当于[0.n,1.n,2.n]
plt.plot(triangle[:,0],triangle[:,1],color='k')
#平移矩阵
transX,transY=(input("请输入你要平移的x,y分量：").split())
transX,transY=float(transX),float(transY)
transMat=np.eye(3)
transMat[2,0],transMat[2,1]=transX,transY
print(transMat)
#缩放矩阵
scaleX,scaleY,sx,sy=(input("请输入缩放的倍数x,y(允许非等比缩放)和缩放中心x,y(一般为重心):").split())
scaleX,scaleY,sx,sy=float(scaleX),float(scaleY),float(sx),float(sy)
Mat0=np.eye(3)
InverseMat0=np.eye(3)
scaleMat=np.eye(3)
#将三个矩阵按顺序组合在一起便可以实现绕点缩放效果
Mat0[2,0],Mat0[2,1]=-sx,-sy
scaleMat[0,0],scaleMat[1,1]=scaleX,scaleY
InverseMat0[2,0],InverseMat0[2,1]=sx,sy
ScaleMat=np.matmul(np.matmul(Mat0,scaleMat),InverseMat0)
#旋转矩阵
rotateX,rotateY,radians=(input("请输入绕点旋转中心坐标x,y和角度radians:").split())
rotateX,rotateY,radians=float(rotateX),float(rotateY),float(radians)
radians=3.1415926*radians/180
Mat=np.eye(3)
InverseMat=np.eye(3)
rotateMat=np.eye(3)
#将三个矩阵按顺序组合在一起便可以实现绕点旋转效果
Mat[2,0],Mat[2,1]=-rotateX,-rotateY
rotateMat[0,0],rotateMat[0,1],rotateMat[1,0],rotateMat[1,1]=math.cos(radians),-math.sin(radians),math.sin(radians),math.cos(radians)
InverseMat[2,0],InverseMat[2,1]=rotateX,rotateY
MultiMat=np.matmul(np.matmul(Mat,rotateMat),InverseMat)
    
triangle=np.dot(np.dot(np.dot(triangle,ScaleMat),MultiMat),transMat)
plt.plot(triangle[:,0],triangle[:,1],color='r')
plt.show()