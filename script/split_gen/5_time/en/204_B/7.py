def main():
    num = int(input())
    nuts = list(map(int, input().split()))
    total = 0
    for n in nuts:
        if n > 10:
            total += n - 10
    print(total)
