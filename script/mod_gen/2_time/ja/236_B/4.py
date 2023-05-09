def main():
    N = int(input())
    A = list(map(int, input().split()))
    S = set()
    for i in range(len(A)):
        if A[i] in S:
            S.remove(A[i])
        else:
            S.add(A[i])
    print(S.pop())

if __name__ == '__main__':
    main()