def main():
    N = int(input())
    A = list(map(int, input().split()))
    if N == 2:
        print("Yes")
        print("1 1")
        print("1 2")
        return
    for i in range(N):
        for j in range(i+1, N):
            for k in range(N):
                for l in range(k+1, N):
                    if i != k and j != l:
                        if (A[i] + A[j]) % 200 == (A[k] + A[l]) % 200:
                            print("Yes")
                            print("2", i+1, j+1)
                            print("2", k+1, l+1)
                            return
    print("No")
