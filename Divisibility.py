N = int(input())

data = [int(x) for x in input().split()]

def div (lst):

    lst1= [i%10 for i in lst]

    num= int(''.join(map(str,lst1)))

    if num%10==0:

        return "Yes"

    else:

        return "No"

print(div(data))
