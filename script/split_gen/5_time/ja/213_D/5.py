def main():
    n = int(input())
    ab = []
    for _ in range(n-1):
        ab.append(list(map(int, input().split())))
    ab = sorted(ab, key=lambda x: x[1])
    ab = sorted(ab, key=lambda x: x[0])
    ab = sorted(ab, key=lambda x: x[1], reverse=True)
    ab = sorted(ab, key=lambda x: x[0], reverse=True)
    ans = []
    ans.append(1)
    ans.append(ab[0][1])
    for i in range(1, n-1):
        if ans[-1] == ab[i][0]:
            ans.append(ab[i][1])
        else:
            ans.append(ab[i][0])
            ans.append(ab[i][1])
    ans.append(1)
    print(' '.join(map(str, ans)))
