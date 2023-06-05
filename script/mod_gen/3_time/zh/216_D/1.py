def main():
    n, m = map(int, input().split())
    k = [0] * m
    a = [[] for _ in range(m)]
    for i in range(m):
        k[i] = int(input())
        a[i] = list(map(int, input().split()))
    #print(n, m, k, a)
    color = [0] * (n+1)
    for i in range(m):
        color[a[i][0]] += 1
    #print(color)
    for i in range(1, n+1):
        if color[i] != 2:
            print('No')
            return
    print('Yes')

if __name__ == '__main__':
    main()