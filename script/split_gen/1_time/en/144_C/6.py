def main():
    N = int(input())
    for i in range(1, N+1):
        if N <= i*(i+1):
            print(i-1 + N - i*(i+1))
            break
