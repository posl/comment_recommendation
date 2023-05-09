def main():
    N = int(input())
    S = [input() for _ in range(N)]
    ans = 'Yes' if S.count('For') > N // 2 else 'No'
    print(ans)

if __name__ == '__main__':
    main()