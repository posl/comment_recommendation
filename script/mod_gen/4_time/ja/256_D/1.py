def main():
    N = int(input())
    Ls = []
    Rs = []
    for _ in range(N):
        L, R = map(int, input().split())
        Ls.append(L)
        Rs.append(R)
    Ls.sort()
    Rs.sort()
    L = Ls[0]
    R = Rs[-1]
    print(L, R+1)

if __name__ == '__main__':
    main()