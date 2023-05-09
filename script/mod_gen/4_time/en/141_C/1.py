def main():
    n,k,q = map(int,input().split())
    a = [k-q for i in range(n)]
    for i in range(q):
        a[int(input())-1] += 1
    for i in range(n):
        print("Yes" if a[i] > 0 else "No")

if __name__ == '__main__':
    main()