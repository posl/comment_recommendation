def main():
    a, b = map(int, input().split())
    for i in range(1, 100000):
        if int(i * 0.08) == a and int(i * 0.1) == b:
            print(i)
            return
    print(-1)
