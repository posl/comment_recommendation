def main():
    N = int(input())
    A = []
    for i in range(N):
        A.append(int(input()))
    max1 = max(A)
    A.remove(max1)
    max2 = max(A)
    for i in range(N):
        if A[i] == max1:
            print(max2)
        else:
            print(max1)

if __name__ == '__main__':
    main()