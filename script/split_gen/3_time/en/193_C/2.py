def main():
    N = int(input())
    ans = 0
    for i in range(2, N+1):
        for j in range(2, N+1):
            if i**j > N:
                break
            ans += 1
    print(N - ans)
    return
main()
