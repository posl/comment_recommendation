def main():
    N = int(input())
    A = list(map(int, input().split()))
    X = int(input())
    B = A * 100
    sumB = sum(B)
    if sumB > X:
        k = 0
        sumBk = 0
        while sumBk <= X:
            sumBk += B[k]
            k += 1
        print(k)
    else:
        k = 0
        sumBk = 0
        while sumBk <= X:
            sumBk += B[k]
            k += 1
        print(k + (X - sumBk) // sumB * N)
main()

if __name__ == '__main__':
    main()