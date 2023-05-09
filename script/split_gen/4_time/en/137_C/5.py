def solve():
    N = int(input())
    l = []
    for i in range(N):
        s = input()
        l.append(''.join(sorted(s)))
    l.sort()
    ans = 0
    count = 1
    for i in range(1,N):
        if l[i-1] == l[i]:
            count += 1
        else:
            ans += count * (count-1) // 2
            count = 1
    ans += count * (count-1) // 2
    print(ans)
