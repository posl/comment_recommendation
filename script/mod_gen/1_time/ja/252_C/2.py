def main():
    N = int(input())
    S = [input() for _ in range(N)]
    ans = 0
    for i in range(10):
        ans = max(ans, S.count(str(i)))
    print(ans * 10)

if __name__ == '__main__':
    main()