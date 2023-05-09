def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    B = []
    C = []
    for i in range(N):
        for j in range(i+1, N):
            if A[i] % 200 == A[j] % 200:
                B = [i+1, j+1]
                C = [i+1, j+1]
    if B == []:
        print("No")
    else:
        print("Yes")
        print(len(B), *B, sep=" ")
        print(len(C), *C, sep=" ")
    return

if __name__ == '__main__':
    main()