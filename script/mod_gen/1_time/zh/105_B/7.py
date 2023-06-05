def solve():
    N = int(input())
    for i in range(0, N//4 + 1):
        for j in range(0, N//7 + 1):
            if i*4 + j*7 == N:
                print("Yes")
                exit()
    print("No")

if __name__ == '__main__':
    solve()