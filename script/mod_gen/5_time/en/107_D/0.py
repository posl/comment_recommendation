def main():
    n = int(input())
    a = list(map(int, input().split()))
    m = []
    for i in range(n):
        for j in range(i, n):
            m.append(sorted(a[i:j+1])[(j-i)//2])
    print(sorted(m)[len(m)//2])

if __name__ == '__main__':
    main()