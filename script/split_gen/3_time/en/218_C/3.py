def main():
    n = int(input())
    s = [input() for _ in range(n)]
    t = [input() for _ in range(n)]
    for i in range(4):
        if s == t:
            print('Yes')
            return
        else:
            s = rotate(s)
    print('No')
