def main():
    n, k, q = map(int, input().split())
    a = [int(input()) for _ in range(q)]
    p = [k-q for _ in range(n)]
    for i in a:
        p[i-1] += 1
    for i in p:
        if i <= 0:
            print("No")
        else:
            print("Yes")
main()

if __name__ == '__main__':
    main()