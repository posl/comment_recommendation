def main():
    N = int(input())
    H = list(map(int, input().split()))
    for i in range(1, N):
        if H[i - 1] < H[i]:
            H[i] -= 1
        if H[i - 1] > H[i]:
            print("No")
            return
    print("Yes")
main()

if __name__ == '__main__':
    main()