def main():
    n = input()
    a = map(int, raw_input().split())
    b = [0] * n
    for i in range(n):
        b[a[i] - 1] = i + 1
    print " ".join(map(str, b))
