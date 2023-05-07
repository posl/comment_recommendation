def main():
    N = int(input())
    a = list(map(int,input().split()))
    cnt = 0
    while all([i % 2 == 0 for i in a]):
        cnt += 1
        a = [i // 2 for i in a]
    print(cnt)
