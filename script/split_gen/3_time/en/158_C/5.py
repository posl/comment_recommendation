def main():
    A, B = map(int, input().split())
    for x in range(1, 100000):
        if A == int(x * 0.08) and B == int(x * 0.1):
            print(x)
            return
    print(-1)
