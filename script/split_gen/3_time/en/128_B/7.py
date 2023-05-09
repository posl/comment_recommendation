def main():
    n = int(input())
    r = []
    for i in range(n):
        s, p = input().split()
        r.append([s, int(p), i + 1])
    r.sort(key=lambda x: (-x[1], x[0], x[2]))
    for i in range(n):
        print(r[i][2])
main()
