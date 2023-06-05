def main():
    n = int(input())
    A = list(map(int, input().split()))
    X = int(input())
    B = A * (10 ** 100)
    sum = 0
    i = 0
    while sum < X:
        sum += B[i]
        i += 1
    print(i)
