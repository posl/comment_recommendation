def main():
    S = input()
    a, b = map(int, input().split())
    ans = S[:a-1] + S[b-1] + S[a:b-1] + S[a-1] + S[b:]
    print(ans)

if __name__ == '__main__':
    main()