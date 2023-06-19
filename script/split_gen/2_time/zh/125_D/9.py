def main():
    N = int(input())
    A = list(map(int, input().split()))
    cnt = 0
    for a in A:
        if a < 0:
            cnt += 1
    if cnt % 2 == 0:
        print(sum(map(abs, A)))
    else:
        print(sum(map(abs, A)) - min(map(abs, A)) * 2)
