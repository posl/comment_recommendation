def main():
    X, Y, N = [int(x) for x in input().split()]
    result = 0
    for i in range(0, N+1):
        if (i % 3 == 0):
            result += X
        else:
            result += Y
    print(result)
