def main():
    N,M = map(int,input().split())
    k = []
    a = []
    for i in range(M):
        k.append(int(input()))
        a.append(list(map(int,input().split())))
    print(N,M)
    print(k)
    print(a)
    print("Yes")
    print("No")

if __name__ == '__main__':
    main()