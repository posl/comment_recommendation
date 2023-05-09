def main():
    N, M = map(int, input().split())
    if M == N - 1:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()