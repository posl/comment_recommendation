def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    for i in range(0, len(A), 2):
        if i == len(A) - 1:
            print(A[i])
        elif A[i] != A[i + 1]:
            print(A[i])
            break

if __name__ == '__main__':
    main()