def main():
    N = int(input())
    ans = 0
    for i in range(3,N+1):
        ans += (N-i)//i + 1
    print(ans%1000000007)
