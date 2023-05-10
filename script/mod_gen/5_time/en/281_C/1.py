def main():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    sum = 0
    count = 0
    for a in A:
        sum += a
        if sum > T:
            break
        count += 1
    print(count, T - sum + A[count - 1])

if __name__ == '__main__':
    main()