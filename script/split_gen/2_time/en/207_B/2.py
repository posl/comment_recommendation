def main():
    A, B, C, D = map(int, input().split())
    if B >= C * D:
        print(-1)
    else:
        count = 0
        while A > C * D:
            A += B
            count += 1
        print(count)
