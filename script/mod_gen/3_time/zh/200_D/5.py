def solve():
    N = int(input())
    A = list(map(int, input().split()))
    sum_A = sum(A)
    mod_A = [a % 200 for a in A]
    mod_A.sort()
    for i in range(N):
        if i == N - 1 or mod_A[i] != mod_A[i + 1]:
            continue
        elif i == N - 2 or mod_A[i] != mod_A[i + 2]:
            continue
        else:
            print("Yes")
            print(1, i + 1)
            print(1, i + 2)
            return
    if sum_A % 200 == 0:
        print("Yes")
        print(1, 1)
        print(1, 2)
    else:
        print("No")

if __name__ == '__main__':
    solve()