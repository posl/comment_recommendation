def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()  # 逆順にしたいので降順にソート
    A.reverse()
    ans = 0
    for i in range(N):
        if i % 2 == 0:
            ans += A[i]
        else:
            ans -= A[i]
    print(ans)
