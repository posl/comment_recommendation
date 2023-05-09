def main():
    n = int(input())
    list = []
    for i in range(n):
        s, p = input().split()
        list.append((s, int(p), i + 1))
    list.sort(key=lambda x: (x[0], -x[1]))
    for i in range(n):
        print(list[i][2])
