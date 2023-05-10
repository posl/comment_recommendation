def main():
    n = int(input())
    v = list(map(int, input().split()))
    v1 = v[::2]
    v2 = v[1::2]
    c1 = max(v1, key=v1.count)
    c2 = max(v2, key=v2.count)
    if c1 == c2:
        if len(set(v1)) == 1:
            v2 = v[2::2]
            c2 = max(v2, key=v2.count)
            print(len([v[i] for i in range(len(v)) if i % 2 == 0 and v[i] != c2]))
        elif len(set(v2)) == 1:
            v1 = v[1::2]
            c1 = max(v1, key=v1.count)
            print(len([v[i] for i in range(len(v)) if i % 2 == 1 and v[i] != c1]))
        else:
            v1 = v[1::2]
            v2 = v[2::2]
            c1 = max(v1, key=v1.count)
            c2 = max(v2, key=v2.count)
            print(len([v[i] for i in range(len(v)) if i % 2 == 0 and v[i] != c2]) + len([v[i] for i in range(len(v)) if i % 2 == 1 and v[i] != c1]))
    else:
        print(len([v[i] for i in range(len(v)) if i % 2 == 0 and v[i] != c1]) + len([v[i] for i in range(len(v)) if i % 2 == 1 and v[i] != c2]))
