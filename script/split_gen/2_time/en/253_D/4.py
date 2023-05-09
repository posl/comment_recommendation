def main():
    N, A, B = map(int, input().split())
    sum = 0
    for i in range(1, N+1):
        if i % A != 0 and i % B != 0:
            sum += i
    print(sum)
