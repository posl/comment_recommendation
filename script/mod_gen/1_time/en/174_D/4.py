def main():
    N = int(input())
    S = input()
    print(min(S[:i].count("R") + S[i:].count("W") for i in range(N+1)))

if __name__ == '__main__':
    main()