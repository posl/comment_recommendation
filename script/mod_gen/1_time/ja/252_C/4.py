def main():
    N = int(input())
    S = [input() for i in range(N)]
    ans = 0
    for i in range(10):
        ans = max(ans, min([S[j].index(str(i)) for j in range(N)]))
    print(ans + 10)

if __name__ == '__main__':
    main()