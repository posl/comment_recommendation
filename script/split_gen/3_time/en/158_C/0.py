def main():
    A, B = map(int, input().split())
    for i in range(1, 1000):
        if int(i * 0.08) == A and int(i * 0.1) == B:
            print(i)
            return
    print(-1)
