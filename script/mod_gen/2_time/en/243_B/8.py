def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    a2b = {}
    for i in range(N):
        a2b[A[i]] = B[i]
    a2i = {}
    for i in range(N):
        a2i[A[i]] = i
    b2i = {}
    for i in range(N):
        b2i[B[i]] = i
    same = 0
    diff = 0
    for i in range(N):
        if A[i] == B[i]:
            same += 1
        else:
            if a2i[B[i]] == b2i[A[i]]:
                diff += 1
    print(same)
    print(diff)

if __name__ == '__main__':
    main()