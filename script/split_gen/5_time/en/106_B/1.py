def main():
    n = int(input())
    count = 0
    for i in range(1, n+1, 2):
        divisor = 0
        for j in range(1, n+1):
            if i % j == 0:
                divisor += 1
        if divisor == 8:
            count += 1
    print(count)
