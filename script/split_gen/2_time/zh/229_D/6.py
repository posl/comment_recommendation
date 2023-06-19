def main():
    S = input()
    K = int(input())
    N = len(S)
    if K == 0:
        ans = 0
        count = 0
        for s in S:
            if s == "X":
                count += 1
            else:
                ans = max(ans, count)
                count = 0
        ans = max(ans, count)
        print(ans)
        return
    ans = 0
    count = 0
    for s in S:
        if s == "X":
            count += 1
        else:
            ans = max(ans, count)
            count = 0
    ans = max(ans, count)
    if K >= 2:
        count = 0
        for s in S:
            if s == "X":
                count += 1
            else:
                ans = max(ans, count + 1)
                count = 0
        ans = max(ans, count + 1)
    print(ans)
