def main():
    N = int(input())
    L = list(map(int, input().split()))
    L.sort()
    ans = 0
    for i in range(N-1):
        for j in range(i+1, N):
            a = L[i]
            b = L[j]
            k = j
            while k < N-1:
                if a+b <= L[k+1]:
                    break
                k += 1
            ans += k - j
    print(ans)
