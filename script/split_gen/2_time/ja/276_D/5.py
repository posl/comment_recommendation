def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    while True:
        if all([a % 2 == 0 for a in A]):
            A = [a // 2 for a in A]
            ans += 1
        else:
            break
    if all([a == A[0] for a in A]):
        print(ans)
    else:
        print(-1)
