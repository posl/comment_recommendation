def main():
    N = int(input())
    V = [int(i) for i in input().split()]
    C = [int(i) for i in input().split()]
    ans = 0
    for i in range(N):
        if V[i] - C[i] > 0:
            ans += V[i] - C[i]
    print(ans)

if __name__ == '__main__':
    main()