def main():
    S = input()
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    print(S[:a] + S[b] + S[a + 1:b] + S[a] + S[b + 1:])

if __name__ == '__main__':
    main()