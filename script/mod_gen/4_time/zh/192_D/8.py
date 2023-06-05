def base_n_to_10(x, n):
    out = 0
    for i in x:
        out = out * n + int(i)
    return out
x = input()
m = int(input())
d = max(x)
d = int(d)
ans = 0

if __name__ == '__main__':
    base_n_to_10()