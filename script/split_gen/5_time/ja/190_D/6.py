def main():
    n = int(input())
    import math
    count = 0
    for i in range(1, int(math.sqrt(n*2)) + 1):
        if (n * 2) % i == 0:
            if (n * 2 // i - i + 1) % 2 == 0:
                count += 1
    print(count * 2)
