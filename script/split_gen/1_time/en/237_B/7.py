def main():
    h,w = map(int, input().split())
    a = []
    for i in range(h):
        a.append(list(map(int, input().split())))
    for i in range(w):
        ans = []
        for j in range(h):
            ans.append(str(a[j][i]))
        print(" ".join(ans))
