def main():
    N = int(input())
    A = list(map(int, input().split()))
    #A = [123, 223, 123, 523, 200, 2000]
    #N = 6
    count = 0
    for i in range(N):
        for j in range(i+1, N):
            if (A[i] - A[j]) % 200 == 0:
                count += 1
    print(count)
