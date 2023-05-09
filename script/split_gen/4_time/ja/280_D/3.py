def main():
    K = int(input())
    N = 1
    for i in range(2, K+1):
        N *= i
        if N % K == 0:
            print(i)
            break
