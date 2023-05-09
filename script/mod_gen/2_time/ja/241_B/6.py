def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()
    #print(A)
    #print(B)
    for i in range(M):
        if B[i] not in A:
            print("No")
            return
    print("Yes")
    return

if __name__ == '__main__':
    main()