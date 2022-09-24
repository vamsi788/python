def minsquares(n):
    if n<=3:
        return n
    res=n
    for x in range(1,n+1):
        temp=x*x;
        if temp>n:
            break
        else:
              res=min(res,1+getminsquares(n-temp))
    return res;
s=int(input("enter number"))
print(getminsquares(s))
