def main():
    n, q = map(int, input().split())
    s = input()
    l = [0] * n
    for i in range(n - 1):
        if s[i] == 'A' and s[i + 1] == 'C':
            l[i + 1] = l[i] + 1
        else:
            l[i + 1] = l[i]
    for i in range(q):
        lft, rght = map(int, input().split())
        print(l[rght - 1] - l[lft - 1])
