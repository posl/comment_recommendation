def main():
    num = int(input())
    nuts = list(map(int, input().split()))
    total = 0
    for nut in nuts:
        if nut >= 10:
            total += nut - 10
    print(total)
