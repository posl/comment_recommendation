def main():
    n = int(input())
    v = list(map(int, input().split()))
    v1 = v[0::2]
    v2 = v[1::2]
    c1 = 0
    c2 = 0
    v1c = max(v1, key=v1.count)
    v2c = max(v2, key=v2.count)
    for i in range(n//2):
        if v1[i] != v1c:
            c1 += 1
        if v2[i] != v2c:
            c2 += 1
    if v1c != v2c:
        print(c1+c2)
    else:
        if c1 < c2:
            print(c1 + min(c1, c2+1))
        else:
            print(c2 + min(c2, c1+1))
