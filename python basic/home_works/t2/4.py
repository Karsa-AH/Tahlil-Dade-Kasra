import jdatetime
now=jdatetime.datetime.now()
a=input("enter your birth date in yyyy-mm-dd : ")
s=jdatetime.datetime.strptime(a,"%Y-%m-%d")
s=now-s 
days=s.days % 7
n=int(now.strftime("%w"))
print( days , n)
f=n-days
if(f<0):
    print(6+(f+1))
else:
    print(f)    
    
#0 is saturday ... and 6 is friday     