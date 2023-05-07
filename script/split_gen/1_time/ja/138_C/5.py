def main():
    N = int(input())
    v = list(map(int, input().split()))
    v.sort()
    while len(v) > 1:
        v1 = v.pop(0)
        v2 = v.pop(0)
        v.append((v1 + v2) / 2)
        v.sort()
    print(v[0])
