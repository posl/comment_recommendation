def main():
    S = input()
    Q = int(input())
    for i in range(Q):
        t, k = map(int, input().split())
        if t % 3 == 0:
            print(S[(k-1) % len(S)])
        elif t % 3 == 1:
            if S[(k-1) % len(S)] == 'A':
                print('B')
            elif S[(k-1) % len(S)] == 'B':
                print('C')
            else:
                print('A')
        else:
            if S[(k-1) % len(S)] == 'A':
                print('C')
            elif S[(k-1) % len(S)] == 'B':
                print('A')
            else:
                print('B')
