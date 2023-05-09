def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.reverse()
    sumA = sum(A)
    if sumA >= 360:
        print(sumA - 360)
    else:
        print(sumA)

if __name__ == '__main__':
    main()