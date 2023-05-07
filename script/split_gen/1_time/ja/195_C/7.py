def main():
    N = int(input())
    i = 1
    res = 0
    while i <= N:
        res += (N - i + 1) * (len(str(i)) - 1) // 3
        i *= 1000
    print(res)
