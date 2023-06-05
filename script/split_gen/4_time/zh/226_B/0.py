def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(list(map(int, input().split()[1:])))
    al = set()
    for i in range(n):
        al.add(tuple(a[i]))
    print(len(al))
