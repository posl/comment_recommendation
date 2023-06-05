def main():
    import sys
    N = int(sys.stdin.readline())
    print(N)
    count = 0
    for i in range(1, N+1):
        if N % i == 0:
            count += 1
    print(count)
