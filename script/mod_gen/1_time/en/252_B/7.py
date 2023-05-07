def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort(reverse=True)
    B.sort()
    i = 0
    for b in B:
        if A[i] > A[b-1]:
            print("Yes")
            return
        i += 1
    print("No")

if __name__ == '__main__':
    main()