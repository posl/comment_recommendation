def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(set(A))
    B.sort()
    ans = 0
    for i in range(len(B)):
        ans += i
    print(ans)
