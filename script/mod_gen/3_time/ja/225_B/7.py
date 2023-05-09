def main():
    N = int(input())
    a = []
    b = []
    for i in range(N-1):
        line = list(map(int, input().split()))
        a.append(line[0])
        b.append(line[1])
    if a.count(a[0]) + b.count(a[0]) == N-1:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()