def main():
    n = int(input())
    h = list(map(int, input().split()))
    cnt = 0
    max_h = 0
    for i in h:
        if i >= max_h:
            cnt += 1
            max_h = i
    print(cnt)
