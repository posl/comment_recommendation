def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()
    i = 0
    for b in B:
        while i < N and A[i] < b:
            i += 1
        if i == N or A[i] != b:
            print("No")
            return
        i += 1
    print("Yes")

if __name__ == '__main__':
    main()