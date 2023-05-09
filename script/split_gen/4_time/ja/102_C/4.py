def main():
    N = int(input())
    A = list(map(int, input().split()))
    # すぬけ君の悲しさの値の最小値は、
    # 中央値になる
    A.sort()
    B = []
    for i in range(N):
        B.append(A[i] - (i+1))
    B.sort()
    b = B[N//2]
    ans = 0
    for i in range(N):
        ans += abs(A[i] - (b+i+1))
    print(ans)
