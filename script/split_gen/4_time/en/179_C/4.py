def main():
    N = int(input())
    count = 0
    for i in range(1, N):
        if N % i == 0:
            count += N // i - 1
    print(count)
