def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    B = [int(i) for i in input().split()]
    if sum([A[i]*B[i] for i in range(N)]) == 0:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()