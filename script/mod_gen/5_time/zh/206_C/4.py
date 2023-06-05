def main():
    N = int(input())
    A = list(map(int,input().split()))
    A.sort()
    i = 0
    j = 0
    count = 0
    while j < N:
        if A[i] == A[j]:
            j += 1
        else:
            count += j - i
            i += 1
    count += (j - i) * (j - i - 1) // 2
    print(count)

if __name__ == '__main__':
    main()