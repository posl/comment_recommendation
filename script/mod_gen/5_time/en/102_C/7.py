def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    b = A[N//2]
    sad = 0
    for a in A:
        sad += abs(a - b)
    print(sad)

if __name__ == '__main__':
    main()