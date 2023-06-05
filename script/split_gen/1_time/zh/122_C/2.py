def main():
    n, q = map(int, input().split())
    s = input()
    ac = [0] * n
    for i in range(n - 1):
        ac[i + 1] = ac[i] + (1 if s[i:i + 2] == 'AC' else 0)
    for i in range(q):
        l, r = map(int, input().split())
        print(ac[r - 1] - ac[l - 1])
