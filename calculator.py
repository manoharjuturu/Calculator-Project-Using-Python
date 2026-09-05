def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if b==0:
        return'error'
    return a/b
def power(a,b):
    return a**b
n1=int(input())
n2=int(input())
print('select option')
print('1.Addition')
print('2.Substration')
print('3.Multiplication')
print('4.Division')
print('5.power')
option=int(input('Enter Option'))
if option==1:
    print(add(n1,n2))
if option==2:
    print(sub(n1,n2))
if option==3:
    print(mul(n1,n2))
if option==4:
    print(div(n1,n2))
if option==5:
    print(power(n1,n2))
else:
    print('Invalid Operation')