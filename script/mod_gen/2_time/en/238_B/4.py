def main():
    N = int(input())
    A = list(map(int, input().split()))
    C = 0
    for i in range(N):
        C += A[i]
    print((360-C)%360)
main()

if __name__ == '__main__':
    main()