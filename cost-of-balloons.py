num=int(input())
while(num>0):
    c1, c2 = map(int,input().split(' '))
    soI=0
    soJ=0
    n=int(input())
    while n>0:
        i,j=map(int,input().split(' '))
        if i==1 or j==1:
            soI+=i
            soJ+=j

        n-=1
    a = c1 * soI + c2 * soJ
    b = c1 * soJ + c2 * soI
    if (a < b):
        print(a)
    else:
        print(b)
    num-=1
