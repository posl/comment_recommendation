def main():
    n = int(input())
    l = []
    for i in range(n):
        l.append(list(map(int, input().split())))
    l.sort(key=lambda x: x[0])
    count = 1
    for i in range(1, n):
        if l[i] != l[i-1]:
            count += 1
    print(count)
