def main():
    N = int(input())
    count = 1
    if N == 1:
        print(1)
        return
    for i in range(2, int(N ** 0.5) + 1):
        if N % i == 0:
            count += 1
            if N // i != i:
                count += 1
    print(count)
