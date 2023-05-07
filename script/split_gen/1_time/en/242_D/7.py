def main():
    S = input()
    Q = int(input())
    Qs = []
    for _ in range(Q):
        t, k = map(int, input().split())
        Qs.append((t, k))
    A = S.count('A')
    B = S.count('B')
    C = S.count('C')
    for t, k in Qs:
        if t % 3 == 0:
            if k <= A:
                print('A')
            elif k <= A + B:
                print('B')
            else:
                print('C')
        elif t % 3 == 1:
            if k <= B:
                print('B')
            elif k <= B + C:
                print('C')
            else:
                print('A')
        else:
            if k <= C:
                print('C')
            elif k <= C + A:
                print('A')
            else:
                print('B')
