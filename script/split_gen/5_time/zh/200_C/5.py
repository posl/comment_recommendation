def problems200_c():
    N = int(input())
    A = list(map(int, input().split()))
    A = [a % 200 for a in A]
    a_mod = [0] * 200
    for a in A:
        a_mod[a] += 1
    ans = 0
    for i in range(200):
        ans += a_mod[i] * (a_mod[i] - 1) // 2
    print(ans)
