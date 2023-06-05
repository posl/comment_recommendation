def main():
    n = int(input())
    res = []
    for i in range(n):
        s, p = input().split()
        res.append([s, int(p), i+1])
    res.sort(key=lambda x: (x[0], -x[1]))
    for i in res:
        print(i[2])
