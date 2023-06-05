def main():
    q = int(input())
    ans = 0
    for i in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            ans += query[1] * query[2]
        else:
            print(ans)
            ans = 0
