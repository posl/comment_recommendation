def main():
    n = int(input())
    p = list(map(int, input().split()))
    q = [i for i in range(1, n+1)]
    count = 0
    for i in range(n):
        if p[i] != q[i]:
            count += 1
    if count <= 2:
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()