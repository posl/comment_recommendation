def main():
    n = int(input())
    v = list(map(int, input().split()))
    v1 = v[::2]
    v2 = v[1::2]
    v1.sort()
    v2.sort()
    v1.append(0)
    v2.append(0)
    if v1[-2] == v2[-2]:
        if v1[-3] == v2[-3]:
            print(min(n-v1.count(v1[-2]), n-v2.count(v2[-2])))
        else:
            print(min(n-v1.count(v1[-2]), n-v2.count(v2[-3])))
    else:
        print(min(n-v1.count(v1[-2]), n-v2.count(v2[-2])))
