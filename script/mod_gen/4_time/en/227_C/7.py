def main():
    N = int(input())
    ans = 0
    for a in range(1, N+1):
        ans += N//a
    for b in range(1, N+1):
        ans -= (N//b - 1)*N//b//2
    for c in range(1, N+1):
        ans += (N//c - 1)*N//c*(N//c + 1)//6
    print(ans)
main()

if __name__ == '__main__':
    main()