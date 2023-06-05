def getBitSum(a, s):
    if (a & s == a):
        return "Yes"
    else:
        return "No"
t = int(input())
for i in range(t):
    a, s = map(int, input().split())
    print(getBitSum(a, s))
