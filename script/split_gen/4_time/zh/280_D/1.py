def main():
    K = int(input())
    N = 1
    while True:
        if K * N % 10 == 0:
            break
        else:
            N += 1
    print(N)
