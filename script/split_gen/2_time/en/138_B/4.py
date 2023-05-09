def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print(N, A)
    sum = 0
    for i in range(N):
        sum += 1 / A[i]
    print(1 / sum)
