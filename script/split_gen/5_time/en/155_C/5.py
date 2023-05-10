def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    s.sort()
    s_set = set(s)
    d = {}
    for i in s_set:
        d[i] = 0
    for i in s:
        d[i] += 1
    max = 0
    for i in s_set:
        if d[i] > max:
            max = d[i]
    for i in s_set:
        if d[i] == max:
            print(i)
