import jdatetime
now=jdatetime.datetime.now()
a=input("enter your birth date in yyyy-mm-dd : ")
s=jdatetime.datetime.strptime(a,"%Y-%m-%d")
s=now-s 
days=s.days
y=days//365
days=days-(365*y)
m=days//30
days=days-(30*m)
d=days


w=d//7
d=d-(w*7)
print(f"you have {y} years and {m} month and {w} weeks and {d} days")