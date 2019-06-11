"计算圆的面积"
# ##method1:
# #定义一个方法来计算圆的面积
# def findArea(r):
#     PI = 3.1415926
#     return PI * (r * r)
#
# # 调用方法
# print("圆的面积为 %.6f" % findArea(5))
#
# ##method2:
# r=float(input('please input the radius of the circle:'))
# pi=3.1415926
# area=pi*r**2
# print('the area of circle is %0.6f'%area)

##method3:
import math
r=float(input('please input the radius of the circle:'))
area=math.pi*r**2
print('the area of circle is %0.6f'%area)