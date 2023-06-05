def main():
    n = int(input())
    a = list(map(int, input().split()))
    d = dict()
    for i in a:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    for i in d.keys():
        if d[i] % 2 == 1:
            print(i)
            break
