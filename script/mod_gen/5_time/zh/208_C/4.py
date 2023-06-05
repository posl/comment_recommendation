def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    num = k//n
    res = [num]*n
    k = k%n
    for i in range(k):
        res[i] += 1
    for i in range(n):
        print(res[a.index(i+1)])

if __name__ == '__main__':
    main()