def main():
    N = int(input())
    P = [int(i) for i in input().split()]
    ans = 0
    for i in P:
        ans = max(ans, P[i-2]+1)
    print(ans)
main()
