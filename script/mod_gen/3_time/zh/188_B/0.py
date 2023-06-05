def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    B = [int(x) for x in input().split()]
    sum = 0
    for i in range(N):
        sum += A[i]*B[i]
    if sum == 0:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()