def main():
    A, B, T = [int(x) for x in input().split()]
    total = 0
    for i in range(1, T + 1):
        if i % A == 0:
            total += B
    print(total)
