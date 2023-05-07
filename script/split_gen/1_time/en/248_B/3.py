def main():
    A, B, K = map(int, input().split())
    count = 0
    while A <= B:
        count += 1
        A *= K
    print(count)
