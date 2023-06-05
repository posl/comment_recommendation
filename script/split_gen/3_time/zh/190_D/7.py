def main():
    n = int(input())
    count = 0
    for i in range(1, 10**6):
        if n - i * (i - 1) // 2 <= 0:
            break
        if (n - i * (i - 1) // 2) % i == 0:
            count += 1
    print(count * 2)
