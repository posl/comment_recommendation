def main():
    s = input()
    q = int(input())
    for _ in range(q):
        t, k = map(int, input().split())
        if t % 3 == 0:
            print(s[(k - 1) % len(s)])
        elif t % 3 == 1:
            if s[(k - 1) % len(s)] == 'A':
                print('B')
            elif s[(k - 1) % len(s)] == 'B':
                print('C')
            else:
                print('A')
        else:
            if s[(k - 1) % len(s)] == 'A':
                print('C')
            elif s[(k - 1) % len(s)] == 'B':
                print('A')
            else:
                print('B')
