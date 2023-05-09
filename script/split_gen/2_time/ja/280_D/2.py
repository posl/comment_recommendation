def main():
    K = int(input())
    N = 1
    while True:
        if K % N == 0:
            K = K // N
            N = 1
        else:
            N += 1
        if K == 1:
            break
    print(N)
