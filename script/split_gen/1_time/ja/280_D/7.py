def main():
    K = int(input())
    N = 1
    while True:
        if N % K == 0:
            print(N)
            break
        N += 1
