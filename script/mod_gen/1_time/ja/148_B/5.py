def main():
    N = int(input())
    S, T = input().split()
    print("".join([S[i] + T[i] for i in range(N)]))

if __name__ == '__main__':
    main()