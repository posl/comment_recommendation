def main():
    A, B, C, D = map(int, input().split())
    count = 0
    while A > C * D and B > C:
        A += B
        count += 1
    print(count if count > 0 else -1)
