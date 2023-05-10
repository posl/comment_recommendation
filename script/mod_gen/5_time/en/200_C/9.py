def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [a%200 for a in A]
    A.sort()
    #print(A)
    cnt = 0
    i = 0
    while i < N-1:
        j = i+1
        while j < N:
            if A[i] == A[j]:
                cnt += 1
                j += 1
            else:
                i = j
                break
        if j == N:
            break
    print(cnt)

if __name__ == '__main__':
    main()