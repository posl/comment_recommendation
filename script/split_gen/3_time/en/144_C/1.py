def main():
    N = int(input())
    i = 1
    while i * (i + 1) <= 2 * N:
        i += 1
    if i * (i - 1) // 2 == N:
        print(2 * i - 3)
    else:
        print(2 * i - 2)
