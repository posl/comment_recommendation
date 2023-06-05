def main():
    n,q = map(int, input().split())
    a = list(map(int, input().split()))
    k = []
    for i in range(q):
        k.append(int(input()))
    a.sort()
    ans = []
    for i in range(q):
        tmp = k[i]
        for j in range(n):
            if tmp < a[j]:
                ans.append(tmp)
                break
            else:
                tmp += 1
                continue
        else:
            ans.append(tmp)
    for i in range(q):
        print(ans[i])
