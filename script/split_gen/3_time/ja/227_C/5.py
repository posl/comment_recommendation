def main():
    N = int(input())
    ans = 0
    for a in range(1,N+1):
        for b in range(a,N//a+1):
            ans += N//(a*b)
    print(ans)
