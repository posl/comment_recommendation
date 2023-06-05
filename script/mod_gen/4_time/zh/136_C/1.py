def main():
    N = int(input())
    H = [int(x) for x in input().split()]
    for i in range(N - 1):
        if H[i] > H[i + 1]:
            H[i] -= 1
    for i in range(N - 1):
        if H[i] > H[i + 1]:
            print("No")
            exit()
    print("Yes")

if __name__ == '__main__':
    main()