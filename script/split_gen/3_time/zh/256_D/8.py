def main():
    n = int(input())
    lr_list = []
    for _ in range(n):
        l, r = map(int, input().split())
        lr_list.append((l, r))
    lr_list.sort()
    ans = []
    l, r = lr_list[0][0], lr_list[0][1]
    for i in range(1, n):
        if lr_list[i][0] <= r:
            r = max(r, lr_list[i][1])
        else:
            ans.append((l, r))
            l, r = lr_list[i][0], lr_list[i][1]
    ans.append((l, r))
    print(*ans, sep='\n')
