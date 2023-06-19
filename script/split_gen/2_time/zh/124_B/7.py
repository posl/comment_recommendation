def main():
    N = int(input())
    H = list(map(int, input().split()))
    cnt = 0
    for i in range(N):
        flag = True
        for j in range(i):
            if H[i] < H[j]:
                flag = False
                break
        if flag:
            cnt += 1
    print(cnt)
