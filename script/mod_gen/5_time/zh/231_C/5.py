def main():
    n,q = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    x = [int(input()) for _ in range(q)]
    for i in range(q):
        print(n - binary_search(a,x[i]) + 1)

if __name__ == '__main__':
    main()