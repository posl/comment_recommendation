def main():
    N = int(input())
    T = list(map(int, input().split()))
    T.sort()
    if N == 1:
        print(T[0])
        return
    if N == 2:
        print(max(T[0], T[1]))
        return
    if N == 3:
        print(max(T[0] + T[1], T[2]))
        return
    if N == 4:
        print(max(T[0] + T[3], T[1] + T[2]))
        return
    if N == 5:
        print(max(T[0] + T[3] + T[4], T[1] + T[2] + T[4]))
        return
    if N == 6:
        print(max(T[0] + T[5] + T[4], T[1] + T[2] + T[3]))
        return
    if N == 7:
        print(max(T[0] + T[1] + T[6] + T[5], T[0] + T[2] + T[3] + T[4]))
        return
    if N == 8:
        print(max(T[0] + T[1] + T[6] + T[7], T[0] + T[2] + T[3] + T[4], T[0] + T[1] + T[2] + T[5]))
        return
    if N == 9:
        print(max(T[0] + T[1] + T[2] + T[3] + T[7] + T[8], T[0] + T[1] + T[2] + T[4] + T[5] + T[8], T[0] + T[1] + T[2] + T[4] + T[6] + T[7]))
        return

if __name__ == '__main__':
    main()