def main():
    N = int(input())
    A = list(map(int, input().split()))
    if N == 1:
        print(max(0, A[0]))
        return
    if N == 2:
        print(max(0, A[0]+A[1]))
        return
    if N == 3:
        print(max(0, A[0]+A[1], A[0]+A[1]+A[2]))
        return
    if N == 4:
        print(max(0, A[0]+A[1], A[0]+A[1]+A[2], A[0]+A[1]+A[2]+A[3]))
        return
    if N == 5:
        print(max(0, A[0]+A[1], A[0]+A[1]+A[2], A[0]+A[1]+A[2]+A[3], A[0]+A[1]+A[2]+A[3]+A[4]))
        return
    if N == 6:
        print(max(0, A[0]+A[1], A[0]+A[1]+A[2], A[0]+A[1]+A[2]+A[3], A[0]+A[1]+A[2]+A[3]+A[4], A[0]+A[1]+A[2]+A[3]+A[4]+A[5]))
        return
    if N == 7:
        print(max(0, A[0]+A[1], A[0]+A[1]+A[2], A[0]+A[1]+A[2]+A[3], A[0]+A[1]+A[2]+A[3]+A[4], A[0]+A[1]+A[2]+A[3]+A[4]+A[5], A[0]+A[1]+A[2]+A[3]+A[4]+A[5]+A[6]))
        return
    if N == 8:
        print(max(0, A[0]+A[1], A[0]+A[1]+A[2], A[0]+A[1]+A[2]+A[3], A[0]+A[1]+

if __name__ == '__main__':
    main()