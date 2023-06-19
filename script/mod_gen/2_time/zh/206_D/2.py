def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    count = 0
    i = 0
    while i < N:
        j = i + 1
        while j < N:
            if A[i] == A[j]:
                count += 1
                i = j + 1
                break
            else:
                j += 1
        i += 1
    if count % 2 == 0:
        print(count)
    else:
        print(count - 1)

if __name__ == '__main__':
    main()