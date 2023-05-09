def main():
    S = input()
    a, b = map(int, input().split())
    S = list(S)
    S[a-1], S[b-1] = S[b-1], S[a-1]
    print("".join(S))

if __name__ == '__main__':
    main()