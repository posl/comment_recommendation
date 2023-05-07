def main():
    N = int(input())
    if N % 2 == 0:
        print(int(N/2 * (N/2-1)))
    else:
        print(int(N/2 * (N/2+1)))
