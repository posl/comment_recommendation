def main():
    N = int(input())
    cnt = 0
    se = set()
    for _ in range(N):
        l = list(map(int, input().split()))
        li = l[1:]
        li.sort()
        li = tuple(li)
        if li not in se:
            se.add(li)
            cnt += 1
    print(cnt)
