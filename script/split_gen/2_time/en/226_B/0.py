def main():
    N = int(input())
    dict = {}
    for i in range(N):
        l = list(map(int, input().split()))
        if l[0] in dict:
            dict[l[0]].append(l[1:])
        else:
            dict[l[0]] = [l[1:]]
    ans = 0
    for i in dict:
        ans += len(set(map(tuple, dict[i])))
    print(ans)
