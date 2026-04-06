#input

name=str(input('enter you name'))
age=int(input('enter your age'))
height=float(input('enter your height'))
sports=str(input('enter your sport'))
gender=str(input('enter your gender'))
print('name',name)
print('age',age)
print('height',height)
print('sports',sports)
print('gender',gender)

print(type(name))
print(type(age))
print(type(gender))
      

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

