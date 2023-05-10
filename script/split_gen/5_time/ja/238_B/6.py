def main():
    N = int(input())
    A = list(map(int,input().split()))
    max = 0
    for i in range(N):
        sum = 0
        for j in range(N):
            sum += A[(i+j)%N]
            if sum > max:
                max = sum
    print(max)
