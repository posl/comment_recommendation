def main():
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    sum = 0
    for i in range(m):
        sum += (i+1)*A[i]
    print(sum)

if __name__ == '__main__':
    main()