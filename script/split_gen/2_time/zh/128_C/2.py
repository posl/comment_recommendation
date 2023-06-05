def main():
    n = int(input())
    rest = []
    for i in range(n):
        s, p = input().split()
        rest.append((s, 100 - int(p), i + 1))
    rest.sort()
    rest.sort(key=lambda x: x[1])
    for i in rest:
        print(i[2])
