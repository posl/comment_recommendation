def check(a,s):
    if s < a:
        return "No"
    if (s-a)%2 == 0:
        return "Yes"
    else:
        return "No"
T = int(input())
for i in range(T):
    a,s = map(int,input().split())
    print(check(a,s))
