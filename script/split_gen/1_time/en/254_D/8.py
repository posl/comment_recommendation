def main():
    N = int(input())
    cnt = 0
    for i in range(1, N+1):
        cnt += N//i
    print(cnt)
