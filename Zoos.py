s = input()
li = [i for i in s]
li1 = [li[i] for i in range(0, len(li)) if li[i] == "z"]
li2 = [li[i] for i in range(0, len(li)) if li[i] == "o"]
if(2 * len(li1)) == len(li2):
  print("YES")
else:
  print("NO")
