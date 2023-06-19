def main():
    n = int(input())
    l = []
    for i in range(n):
        l.append(list(map(int, input().split())))
    l.sort()
    l = [l[0]] + [l[i] for i in range(1, n) if l[i][0] > l[i-1][1]]
    for i in range(len(l)):
        print(l[i][0], l[i][1])
