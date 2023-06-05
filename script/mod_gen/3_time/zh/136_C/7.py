def main():
    N = int(input())
    H = [int(i) for i in input().split(" ")]
    for i in range(1,N):
        if H[i] > H[i-1]:
            H[i] -= 1
    for i in range(1,N):
        if H[i] < H[i-1]:
            print("No")
            return
    print("Yes")

if __name__ == '__main__':
    main()