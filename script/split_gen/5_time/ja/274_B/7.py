def main():
    h, w = map(int, input().split())
    c = [list(input()) for _ in range(h)]
    for i in range(w):
        cnt = 0
        for j in range(h):
            if c[j][i] == "#":
                cnt += 1
        if cnt == 0:
            continue
        print(cnt, end=" ")
    print("")
