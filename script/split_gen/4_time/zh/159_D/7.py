def main():
    n = int(input())
    a = list(map(int, input().split()))
    d = {}
    for i in a:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    ans = sum([v*(v-1)//2 for v in d.values()])
    for i in a:
        print(ans - (d[i]-1))
