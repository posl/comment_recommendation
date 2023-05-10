def main():
    x, n = map(int, input().split())
    p = set(map(int, input().split()))
    for i in range(100):
        if x-i not in p:
            print(x-i)
            return
        elif x+i not in p:
            print(x+i)
            return
