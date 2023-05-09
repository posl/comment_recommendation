def main():
    n = int(input())
    s = [input() for _ in range(n)]
    s.reverse()
    print("\n".join(s))
