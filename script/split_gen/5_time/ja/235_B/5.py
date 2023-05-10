def main():
    N = int(input())
    H = list(map(int, input().split()))
    max_H = 0
    cnt = 0
    for i in range(N-1):
        if H[i] >= H[i+1]:
            cnt += 1
        else:
            if cnt > max_H:
                max_H = cnt
            cnt = 0
    if cnt > max_H:
        max_H = cnt
    print(max_H)
