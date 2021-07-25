def ext(x):

      while(x>0):y,x=x%10,x//10

      return y

 

n=int(input())

num=input().split()

num1=''.join(map(str,(map(ext,map(int,num[0:int(n/2)])))))

num=''.join(map(str,(map(lambda x:x%10,(map(int,num[int(n/2):n]))))))

if int(str(num1)+str(num))%11==0:print("OUI")

else:

       print("NON")
