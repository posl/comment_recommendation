def solve():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    while True:
        if all(a%2==0 for a in A):
            A = [a//2 for a in A]
            ans += 1
        elif any(a%2==0 for a in A):
            print(ans)
            return
        else:
            print(ans)
            return
