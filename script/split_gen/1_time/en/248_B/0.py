def main():
    A, B, K = map(int, input().split())
    count = 0
    while A < B:
        A = A * K
        count += 1
    print(count)
