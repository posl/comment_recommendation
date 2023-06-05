def main():
    i = int(input())
    ss = []
    for ii in range(i):
        ss.append(input())
    ss.sort()
    max = 0
    maxs = []
    for s in ss:
        if ss.count(s) > max:
            max = ss.count(s)
            maxs = [s]
        elif ss.count(s) == max and maxs.count(s) == 0:
            maxs.append(s)
    for s in maxs:
        print(s)
