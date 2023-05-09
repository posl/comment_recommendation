def solve():
    N = int(input())
    ans = 0
    for i in range(1, 10**6+1):
        if i*(i+1)//2 > N:
            break
        if (N-i*(i+1)//2)%i == 0:
            ans += 2
    print(ans)
