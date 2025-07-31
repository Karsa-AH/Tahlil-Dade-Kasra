s=int(input())
m=s//60
s=s-(m*60)
h=m//60
m=m-(h*60)
print(h,m,s)