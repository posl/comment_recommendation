def main():
    n = int(input())
    h = list(map(int, input().split()))
    for i in range(n - 1):
        if h[i + 1] - h[i] >= 2:
            print("No")
            exit()
    print("Yes")

if __name__ == '__main__':
    main()