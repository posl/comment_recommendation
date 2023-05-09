def main():
    N = int(input())
    if N % 2 == 0:
        N -= 1
    cnt = 0
    for i in range(1, N+1, 2):
        if count_divisor(i) == 8:
            cnt += 1
    print(cnt)
