def main():
    # Write code here
    n = int(input())
    p = list(map(int,input().split()))
    q = [0]*n
    for i in range(n):
        q[p[i]-1] = i+1
    print(*q)

if __name__ == '__main__':
    main()