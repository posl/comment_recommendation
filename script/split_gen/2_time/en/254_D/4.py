def main():
    N = int(input())
    ans = 0
    for i in range(1,N+1):
        for j in range(1,N+1):
            if i*j <= N and i == j:
                ans += 1
            elif i*j <= N and i != j:
                ans += 2
            else:
                break
    print(ans)
main()
