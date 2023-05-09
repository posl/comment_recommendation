def main():
    N = int(input())
    cnt = 0
    for i in range(N):
        A, B = map(int, input().split())
        cnt += (B - A + 1) * (A + B) // 2
    print(cnt % (10 ** 9 + 7))
