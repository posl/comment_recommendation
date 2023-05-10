def solve():
    N = int(input())
    T = list(map(int, input().split()))
    if N == 1:
        print(T[0])
        return
    if N == 2:
        print(max(T[0], T[1]))
        return
    if N == 3:
        print(max(T[0] + T[1], T[1] + T[2], T[2] + T[0]))
        return
    if N == 4:
        print(max(T[0] + T[1], T[1] + T[2], T[2] + T[3], T[3] + T[0]))
        return
    if N == 5:
        print(max(T[0] + T[1], T[1] + T[2], T[2] + T[3], T[3] + T[4], T[4] + T[0]))
        return
    if N == 6:
        print(max(T[0] + T[1], T[1] + T[2], T[2] + T[3], T[3] + T[4], T[4] + T[5], T[5] + T[0]))
        return
    if N == 7:
        print(max(T[0] + T[1], T[1] + T[2], T[2] + T[3], T[3] + T[4], T[4] + T[5], T[5] + T[6], T[6] + T[0]))
        return
    if N == 8:
        print(max(T[0] + T[1], T[1] + T[2], T[2] + T[3], T[3] + T[4], T[4] + T[5], T[5] + T[6], T[6] + T[7], T[7] + T[0]))
        return
    if N == 9:
        print(max(T[0] + T[1], T[1] + T[2], T[2] + T[3], T[3] + T[4], T[4] + T[5], T[5] + T[6], T[6] +

if __name__ == '__main__':
    solve()