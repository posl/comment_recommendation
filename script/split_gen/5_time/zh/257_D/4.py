def main():
    n = int(input())
    xy = []
    for i in range(n):
        xy.append(list(map(int, input().split())))
    print(xy)
