def main():
    n, k, q = map(int, input().split())
    a = [int(input()) for _ in range(q)]
    point = [k-q for _ in range(n)]
    for i in range(q):
        point[a[i]-1] += 1
    for i in range(n):
        print("Yes" if point[i] > 0 else "No")

if __name__ == '__main__':
    main()