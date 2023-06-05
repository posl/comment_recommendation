def main():
    n = int(input())
    p = list(map(int,input().split()))
    k = 1
    for i in range(n):
        for j in range(i+1,n):
            if p[i]>p[j]:
                k += 1
    q = [0]*n
    q[0] = k
    for i in range(1,n):
        k = 1
        for j in range(i+1,n):
            if p[i-1]>p[j]:
                k += 1
        q[i] = k
    print(" ".join(map(str,q)))

if __name__ == '__main__':
    main()