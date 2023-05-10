def main():
    n = int(input())
    a = list(map(int, input().split()))
    a = [(i, a[i]) for i in range(len(a))]
    while True:
        if len(a) == 2:
            print(min(a[0], a[1], key=lambda x: x[1])[0] + 1)
            break
        a = [(i, max(a[j], a[j + 1], key=lambda x: x[1])) for i, j in enumerate(range(0, len(a), 2))]
        a = [a[i] for i in range(len(a)) if i % 2 == 0]
    return 0
