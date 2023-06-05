def main():
    N,L = map(int,input().split())
    ans = 0
    min_diff = 1000000000
    for i in range(N):
        ans += L + i
        if abs(L+i) < min_diff:
            min_diff = abs(L+i)
            min_index = i
    print(ans - (L + min_index))
