def main():
    N, D = map(int, input().split())
    L = []
    R = []
    for i in range(N):
        l, r = map(int, input().split())
        L.append(l)
        R.append(r)
    L.sort()
    R.sort()
    ans = 0
    for i in range(N):
        if R[i] - L[i] + 1 >= D:
            ans = N
            break
        if L[i] > R[i-1] + D:
            ans += 1
        elif L[i] <= R[i-1] + D:
            if i == N-1:
                ans += 1
            else:
                if R[i+1] - L[i] + 1 >= D:
                    ans += 1
                else:
                    ans += 2
    print(ans)
