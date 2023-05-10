def main():
    N = int(input())
    A = list(map(int, input().split()))
    X = int(input())
    B = A * 100
    S = sum(B)
    if X < S:
        print(0)
        exit()
    ans = (X // S) * len(B)
    X -= (X // S) * S
    for i in range(len(B)):
        if X < 0:
            print(ans)
            exit()
        X -= B[i]
        ans += 1
