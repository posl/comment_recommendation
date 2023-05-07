def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [a-1 for a in A]
    A = [0] + A
    ans = [0] * (2**N)
    for i in range(1, 2**N):
        ans[i] = ans[A[i]] + 1
    for a in ans:
        print(a)

if __name__ == '__main__':
    main()