def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = a
    for i in range(n - 1):
        tmp = []
        for j in range(0, 2 ** (n - i), 2):
            if b[j] > b[j + 1]:
                tmp.append(b[j])
            else:
                tmp.append(b[j + 1])
        b = tmp
    print(a.index(min(b)) + 1)
