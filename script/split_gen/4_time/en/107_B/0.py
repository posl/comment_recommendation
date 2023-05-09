def main():
    H, W = map(int, input().split())
    a = [input() for _ in range(H)]
    ans = []
    for i in range(H):
        if '#' in a[i]:
            ans.append(a[i])
    ans = [[ans[j][i] for j in range(len(ans))] for i in range(len(ans[0]))]
    for i in range(len(ans)):
        print(''.join(ans[i]))
