def main():
    n = int(input())
    list = []
    for i in range(n):
        list.append(input())
    d = {}
    for i in list:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    print(max(d, key=d.get))
