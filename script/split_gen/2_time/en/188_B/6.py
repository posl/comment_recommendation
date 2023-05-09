def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    B = [int(x) for x in input().split()]
    print("Yes" if sum([A[i]*B[i] for i in range(N)]) == 0 else "No")
