def main():
    K = int(input())
    if K % 2 == 0 or K % 5 == 0:
        print(-1)
        return
    N = 7 % K
    count = 1
    while N != 0:
        N = (N * 10 + 7) % K
        count += 1
    print(count)
