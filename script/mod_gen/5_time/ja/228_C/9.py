def main():
    n, k = map(int, input().split())
    p = [list(map(int, input().split())) for _ in range(n)]
    p_sum = [0] * n
    for i in range(n):
        p_sum[i] = sum(p[i])
    p_sum.sort(reverse=True)
    for i in range(n):
        if p_sum[i] > p_sum[k-1]:
            print("No")
        else:
            print("Yes")

if __name__ == '__main__':
    main()