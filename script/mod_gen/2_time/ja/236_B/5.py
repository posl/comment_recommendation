def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    for i in range(4*N-1):
        if A[i] == A[i+1]:
            i += 1
        else:
            print(A[i])
            break

if __name__ == '__main__':
    main()