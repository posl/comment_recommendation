def main():
    s = input()
    q = int(input())
    a = s.count('A')
    b = s.count('B')
    c = s.count('C')
    for _ in range(q):
        t, k = map(int, input().split())
        t %= 3
        if t == 0:
            if k <= a:
                print('A')
            elif k <= a + b:
                print('B')
            else:
                print('C')
        elif t == 1:
            if k <= b:
                print('B')
            elif k <= a + b:
                print('A')
            else:
                print('C')
        else:
            if k <= c:
                print('C')
            elif k <= a + c:
                print('A')
            else:
                print('B')
