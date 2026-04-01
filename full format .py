#input
name=str(input('enter you name'))
age=int(input('enter your age'))
height=float(input('enter your height'))
sports=str(input('enter your sport'))
gender=str(input('enter your gender'))
print(name)
print(age)
print(height)
print(sports)
print(gender)

#id
print(id(name))
print(id(sports))


#arithmetic +-*/ // %
a=25
b=36
c=69
d=a/c
print(d)

#assignment
c-=d
print(c)

#if else
salary=int(input('enter your salary'))
time=float(input('enter your time'))
if salary>20000 and time>9:
    print("benefit")
else:
    print('not benefit')

#if elif else
income=int(input('enter your income'))
expense=int(input('enter your exp'))

if income>250000 and expense>200000:
    print('good job')
elif income>200000 and expense>180000:
    print('avg job')
elif income>100000 and expense>80000:
    print('bad job')
else:
    print('exit')

#nested if else

a=36
b=28
c=29
d=37


if a>b:
    if a>c:
        if a>d:
            print('a ia greater than all')
        else:
            print('a is greater than all not d')
    else:
        print('a is the greater than b not c')
else:
    print('a is smaller than b')


#leap year

year=2068

if year%4==0:
    if year%100==0:
        if year%400==0:
            print('leap year')
        else:
            print('not leap year')
    else:
        print('leap year')
else:
    print('not leap year')
