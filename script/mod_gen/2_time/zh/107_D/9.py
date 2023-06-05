def main():
    N = int(input())
    a = list(map(int, input().split()))
    b = []
    for i in range(N):
        for j in range(i,N):
            b.append(a[i:j+1])
    b = sorted(b)
    print(b[len(b)//2][len(b[len(b)//2])//2])

if __name__ == '__main__':
    main()