def main():
    n = int(input())
    s = [input() for _ in range(n)]
    print(*s[::-1], sep='
')
