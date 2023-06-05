def main():
    N = int(input())
    i = 1
    count = 0
    while i <= N:
        if N % i == 0:
            if i % 2 != 0 and i % 5 != 0 and i % 3 != 0:
                count += 1
        i += 1
    print(count)
