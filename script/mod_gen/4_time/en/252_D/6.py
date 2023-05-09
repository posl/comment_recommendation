def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    A.append(0)
    cnt = 0
    i = 0
    j = 1
    k = 2
    while i < N-2:
        if A[i] == A[i+1]:
            i += 1
            continue
        j = i+1
        while j < N-1:
            if A[j] == A[j+1]:
                j += 1
                continue
            k = j+1
            while k < N:
                if A[k] == A[k+1]:
                    k += 1
                    continue
                if A[i] != A[j] and A[j] != A[k] and A[k] != A[i]:
                    cnt += 1
                k += 1
            j += 1
        i += 1
    print(cnt)

if __name__ == '__main__':
    main()