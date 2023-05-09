def main():
    N = int(input())
    A = list(map(int, input().split()))
    X = int(input())
    B = A * 10**5
    sum = 0
    for i in range(10**5):
        sum += B[i]
        if sum > X:
            print(i+1)
            exit()
