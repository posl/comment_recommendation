def main():
    n = int(input())
    s = [1]
    for i in range(2, n + 1):
        s = s + [i] + s
    print(*s)
