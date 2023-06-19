def main():
    N, M = map(int, input().split())
    k = []
    for i in range(M):
        k.append(int(input()))
        a = list(map(int, input().split()))
    if N % 2 == 1:
        print("No")
        exit()
    for i in range(M):
        if k[i] % 2 == 1:
            print("No")
            exit()
        for j in range(k[i]):
            if a[j] == a[j + 1]:
                print("No")
                exit()
    print("Yes")

if __name__ == '__main__':
    main()