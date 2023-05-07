def main():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 200
    D = dict()
    for i in range(N):
        key = A[i] % MOD
        if key not in D:
            D[key] = [i]
        else:
            D[key].append(i)
    for key in D:
        if len(D[key]) >= 2:
            print("Yes")
            print(1, D[key][0] + 1)
            print(1, D[key][1] + 1)
            return
    print("No")
