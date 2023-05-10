def main():
    N = int(input())
    B = list(map(int, input().split()))
    A = []
    A.append(B[0])
    for i in range(1,N-1):
        A.append(min(B[i-1],B[i]))
    A.append(B[N-2])
    print(sum(A))
main()

if __name__ == '__main__':
    main()