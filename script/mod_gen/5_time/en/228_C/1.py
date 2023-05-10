def main():
    n, k = map(int, input().split())
    p = []
    for i in range(n):
        p.append(list(map(int, input().split())))
    for i in range(n):
        p[i].append(sum(p[i]))
    p.sort(key=lambda x: x[3], reverse=True)
    print('Yes') if k <= p.index(p[k-1])+1 else print('No')

if __name__ == '__main__':
    main()