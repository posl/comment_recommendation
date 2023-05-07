def main():
    N, M = map(int, input().split())
    A = []
    for _ in range(M):
        k = int(input())
        a = list(map(int, input().split()))
        A.append(a)
    #print(N, M, A)
    B = [0] * N
    for a in A:
        for x in a:
            B[x - 1] += 1
    for b in B:
        if b % 2 != 0:
            print("No")
            return
    print("Yes")
    return

if __name__ == '__main__':
    main()