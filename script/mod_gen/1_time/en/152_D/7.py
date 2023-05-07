def main():
    N = int(input())
    ans = 0
    for i in range(N):
        ans += (N-i)//10 + 1
    print(ans)

if __name__ == '__main__':
    main()