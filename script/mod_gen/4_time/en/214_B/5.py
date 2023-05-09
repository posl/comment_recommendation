def count(a, b, c):
    if (a+b+c <= S) and (a*b*c <= T):
        return 1
    else:
        return 0
S, T = map(int, input().split())
count = 0
for a in range(0, S+1):
    for b in range(0, S+1):
        for c in range(0, S+1):
            count += count(a, b, c)
print(count)

if __name__ == '__main__':
    count()