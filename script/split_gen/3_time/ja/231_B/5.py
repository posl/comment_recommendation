def main():
    N = int(input())
    s = [input() for i in range(N)]
    print(max(set(s), key=s.count))
