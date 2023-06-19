def main():
    N = int(input())
    a = list(map(int, input().split()))
    m = []
    for i in range(N):
        for j in range(i, N):
            m.append(a[i:j+1])
    m.sort()
    print(m[len(m)//2][len(m[len(m)//2])//2])

if __name__ == '__main__':
    main()