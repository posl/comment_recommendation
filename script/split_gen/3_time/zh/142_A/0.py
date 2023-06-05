def main():
    N = int(input())
    if N > 0 and N <= 100:
        if N % 2 == 0:
            print(0.5)
        else:
            print((N+1)/2/N)
