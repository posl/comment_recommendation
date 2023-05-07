def main():
    n = int(input())
    A = list(map(int, input().split()))
    B = [0] * n
    for i in range(n):
        B[i] = abs(A[i])
    ans = sum(B)
    if ans == 0:
        print(0)
    elif ans % 2 == 1:
        print(ans)
    else:
        print(ans - 2 * min(B))

if __name__ == '__main__':
    main()