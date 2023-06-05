def main():
    N = int(input())
    S = input()
    W = list(map(int, input().split()))
    left = 0
    right = 10**9+1
    while right - left > 1:
        mid = (left + right) // 2
        ok = True
        for i in range(N):
            if S[i] == '0' and W[i] >= mid:
                ok = False
        if ok:
            left = mid
        else:
            right = mid
    print(left)
