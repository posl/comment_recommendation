def main():
    N = int(input())
    count = 0
    i = 1
    while i * (i + 1) // 2 <= N:
        if (N - i * (i + 1) // 2) % i == 0:
            count += 1
        i += 1
    print(count * 2)
