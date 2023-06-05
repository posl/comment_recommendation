def main():
    n,k = map(int,input().split())
    p = list(map(int,input().split()))
    p.sort(reverse=True)
    max = 0
    for i in range(k):
        max += p[i]
    max += k
    print(max/2)
    return 0

if __name__ == '__main__':
    main()