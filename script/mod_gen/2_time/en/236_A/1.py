def main():
    S = input()
    a, b = map(int, input().split())
    S = S[:a-1] + S[b-1] + S[a:b-1] + S[a-1] + S[b:]
    print(S)

if __name__ == '__main__':
    main()