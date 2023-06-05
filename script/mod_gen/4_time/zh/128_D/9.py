def main():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    if K > N:
        K = N
    max_sum = 0
    for i in range(K+1):
        for j in range(K+1-i):
            sum = 0
            left = V[:i]
            right = V[N-j:]
            sum = sum + sum(left) + sum(right)
            left.sort()
            right.sort()
            for k in range(min(i, j)):
                if left[k] < right[-1-k]:
                    sum = sum - left[k] + right[-1-k]
            max_sum = max(max_sum, sum)
    print(max_sum)

if __name__ == '__main__':
    main()