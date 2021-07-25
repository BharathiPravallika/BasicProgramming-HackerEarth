n = int(input())
s = input()
if "HH" in s:
    print("NO")
else:
    s2 = ""
    for i in s:
        if i == ".":
            s2 += "B"
        else:
            s2 += "H"
    print("YES")
    print(s2)
