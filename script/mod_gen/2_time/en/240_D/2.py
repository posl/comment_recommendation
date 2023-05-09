def main():
    N = int(input())
    a = list(map(int, input().split()))
    b = []
    for i in range(N):
        b.append(0)
    for i in range(N):
        b[a[i]-1] += 1
    print(b.count(1))

if __name__ == '__main__':
    main()