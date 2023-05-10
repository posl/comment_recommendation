def main():
    q = int(input())
    a = []
    for i in range(q):
        p = list(map(int, input().split()))
        if p[0] == 1:
            a.append(p[1])
        elif p[0] == 2:
            for j in range(len(a)):
                a[j] += p[1]
        else:
            print(min(a))
            a.remove(min(a))
