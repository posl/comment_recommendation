def main():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        s.append(list(input()))
    for i in range(n):
        t.append(list(input()))
    for i in range(4):
        if s == t:
            print('Yes')
            exit()
        s = rotate(s)
    print('No')
