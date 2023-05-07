def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * 200
    C = [0] * 200
    for i in range(N):
        B[A[i] % 200] += 1
    for i in range(200):
        if B[i] >= 2:
            print("Yes")
            print(B[i], end=" ")
            for j in range(N):
                if A[j] % 200 == i:
                    print(j + 1, end=" ")
                    B[i] -= 1
                    if B[i] == 0:
                        break
            print()
            print(B[i], end=" ")
            for j in range(N):
                if A[j] % 200 == i:
                    print(j + 1, end=" ")
                    B[i] -= 1
                    if B[i] == 0:
                        break
            print()
            return
    print("No")

if __name__ == '__main__':
    main()