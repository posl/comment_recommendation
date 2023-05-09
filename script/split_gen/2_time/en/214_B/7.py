def check(a,b,c):
    if a+b+c <= S and a*b*c <= T:
        return True
    else:
        return False
S, T = map(int, input().split())
count = 0
for a in range(S+1):
    for b in range(S+1):
        for c in range(S+1):
            if check(a,b,c):
                count += 1
print(count)
