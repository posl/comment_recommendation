def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    for i in range(N * 4 - 1):
        if A[i] != A[i + 1]:
            print(A[i])
            break
        else:
            i += 3
    else:
        print(A[-1])

if __name__ == '__main__':
    main()