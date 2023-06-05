def main():
    n = int(input())
    d = {}
    for i in range(n):
        s = input()
        if s in d:
            d[s] += 1
        else:
            d[s] = 1
    max = 0
    for k in d:
        if d[k] > max:
            max = d[k]
    l = []
    for k in d:
        if d[k] == max:
            l.append(k)
    l.sort()
    for i in l:
        print(i)
