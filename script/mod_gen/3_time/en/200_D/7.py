def solve():
    N = int(input())
    A = list(map(int, input().split()))
    if N > 200:
        print("No")
        return
    mod200 = [0] * 200
    for i in range(N):
        mod200[A[i] % 200] += 1
    for i in range(200):
        if mod200[i] >= 2:
            print("Yes")
            print(mod200[i], end=" ")
            for j in range(N):
                if A[j] % 200 == i:
                    print(j + 1, end=" ")
                    mod200[i] -= 1
                    if mod200[i] == 0:
                        break
            print()
            print(mod200[i], end=" ")
            for j in range(N):
                if A[j] % 200 == i:
                    print(j + 1, end=" ")
                    mod200[i] -= 1
                    if mod200[i] == 0:
                        break
            print()
            return
    print("No")
    return

if __name__ == '__main__':
    solve()