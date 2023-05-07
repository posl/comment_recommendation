def main():
    N = int(input())
    for i in range(1, N+1):
        if N <= i*(i+1)/2:
            print(i)
            exit()
