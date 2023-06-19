def main():
    n, k = map(int, input().split())
    p = [list(map(int, input().split())) for _ in range(n)]
    p.sort(key=lambda x: sum(x))
    p = list(map(sum, p))
    p.sort(reverse=True)
    for i in range(n):
        if p[i] > p[k - 1]:
            print("No")
        else:
            print("Yes")

if __name__ == '__main__':
    main()