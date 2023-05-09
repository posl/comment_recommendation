def main():
    n = int(input())
    data = []
    for i in range(n):
        data.append(input().split() + [i + 1])
    data.sort(key=lambda x: (x[0], -int(x[1])))
    for d in data:
        print(d[2])
