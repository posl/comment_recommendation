def main():
    A,B = map(int, input().split())
    for i in range(1, 1000):
        if A == int(i*0.08) and B == int(i*0.1):
            print(i)
            return
    print(-1)
