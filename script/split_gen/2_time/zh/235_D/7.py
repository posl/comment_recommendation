def main():
    a, N = map(int, input().split())
    # print(a, N)
    count = 0
    if N % a != 0:
        count += 1
        N = N * a
    while N % 10 == 0:
        count += 1
        N = N // 10
    print(count)
