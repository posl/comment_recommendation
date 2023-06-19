def main():
    N = int(input())
    a = list(map(int, input().split()))
    m = []
    for i in range(N):
        for j in range(i, N):
            m.append(sorted(a[i:j+1])[(j-i+1)//2])
    print(sorted(m)[len(m)//2])

if __name__ == '__main__':
    main()