def check(a,b):
    if a == "W":
        return b == "L"
    elif a == "L":
        return b == "W"
    else:
        return b != "D"
n = int(input())
a = [input() for i in range(n)]
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        if a[i][j] == "-":
            continue
        if check(a[i][j], a[j][i]) == False:
            print("incorrect")
            exit()
print("correct")
