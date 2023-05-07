def main():
    N = int(input())
    C = list(input())
    ans = 0
    for i in range(N):
        if C[i] == 'R':
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()