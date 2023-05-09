def main():
    N = int(input())
    A = list(map(int, input().split()))
    X = int(input())
    sumA = sum(A)
    sumB = (X // sumA) * sumA
    cnt = (X // sumA) * N
    for a in A:
        sumB += a
        cnt += 1
        if sumB > X:
            break
    print(cnt)

if __name__ == '__main__':
    main()