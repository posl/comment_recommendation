def main():
    N = int(input())
    a = []
    b = []
    for i in range(N-1):
        tmp = list(map(int, input().split()))
        a.append(tmp[0])
        b.append(tmp[1])
    a.sort()
    b.sort()
    if a[0] == 1 and b[-1] == N:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()