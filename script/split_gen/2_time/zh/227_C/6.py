def main():
    N = int(input())
    cnt = 0
    for i in range(1, N + 1):
        if i ** 3 <= N:
            cnt += 1
        else:
            break
    print(cnt)
