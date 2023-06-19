def main():
    n = int(input())
    a = [0] * n
    for i in range(n):
        l = list(map(int, input().split()))
        l.pop(0)
        a[i] = tuple(l)
    print(len(set(a)))
    return
