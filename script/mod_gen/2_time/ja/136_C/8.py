def solve():
    N = int(input())
    H = list(map(int, input().split()))
    for i in range(1, N):
        if H[i] >= H[i - 1]:
            continue
        elif H[i] == H[i - 1] - 1:
            H[i] += 1
        else:
            print("No")
            return
    print("Yes")
    return

if __name__ == '__main__':
    solve()