def main():
    n = int(input())
    l = []
    for i in range(n):
        l.append(list(map(int, input().split())))
    l = [tuple(i) for i in l]
    print(len(set(l)))
