def solve():
    N = int(input())
    ans = []
    i = 1
    while i * i <= N:
        if N % i == 0:
            ans.append(i)
            if i != N // i:
                ans.append(N // i)
        i += 1
    ans.sort()
    for a in ans:
        print(a)
