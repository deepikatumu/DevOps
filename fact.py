n=int(input("enter the num"))
factorial=1
if n<0:
    print("not a factorial")
elif n==0:
    print("factorial is 1")
else:
    for i in range(1,n+1):
        factorial=factorial*i
    print("the fact",factorial)
