def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    B = [int(i) for i in input().split()]
    dot = 0
    for i in range(N):
        dot += A[i] * B[i]
    if dot == 0:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()