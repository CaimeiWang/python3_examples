a=float(input('please input the first line:'))
b=float(input('please input the second line:'))
c=float(input('please input the third line:'))
s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c))**0.5
print('the area of triangle is %0.2f'%area)