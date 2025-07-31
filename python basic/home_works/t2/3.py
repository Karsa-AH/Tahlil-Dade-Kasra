import jdatetime
now=jdatetime.datetime.now()
a=input("enter your birth date in yyyy-mm-dd : ")
s=jdatetime.datetime.strptime(a,"%Y-%m-%d")
s=now-s 
print(f"you are {s.days} days old")