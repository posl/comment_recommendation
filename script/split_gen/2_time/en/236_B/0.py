def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * N
    for a in A:
        B[a-1] += 1
    for i in range(N):
        if B[i] % 2 == 1:
            print(i+1)
            exit()
