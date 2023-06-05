def main():
    N = int(input())
    v = [int(i) for i in input().split()]
    v.sort()
    res = v[0]
    for i in range(1, N):
        res = (res + v[i]) / 2
    print(res)
