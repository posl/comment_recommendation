def main():
    N = int(input())
    S = [1]
    for i in range(N):
        S = S + [i+2] + S
    print(*S)

if __name__ == '__main__':
    main()