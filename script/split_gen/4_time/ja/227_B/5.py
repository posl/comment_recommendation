def main():
    n = int(input())
    s = list(map(int, input().split()))
    cnt = 0
    for i in s:
        if i % 6 == 0:
            cnt += 1
        elif i % 10 == 0:
            cnt += 1
        elif i % 15 == 0:
            cnt += 1
        elif i % 21 == 0:
            cnt += 1
        elif i % 35 == 0:
            cnt += 1
        elif i % 55 == 0:
            cnt += 1
    print(cnt)
