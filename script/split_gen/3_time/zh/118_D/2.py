def main():
    n,m = map(int,raw_input().split())
    a = map(int,raw_input().split())
    d = {2:1,5:2,5:3,4:4,5:5,6:6,3:7,7:8,6:9}
    a.sort()
    a.reverse()
    ans = ''
    for i in a:
        ans += str(d[i])
    print int(ans)
