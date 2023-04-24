Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    X, Y, A, B = map(int, input().split())
    ans = 0
    while X * A < Y and X * A < X + B:
        X *= A
        ans += 1
    ans += (Y - X - 1) // B
    print(ans)

=======
Suggestion 2

def main():
    X, Y, A, B = map(int, input().split())
    ans = 0
    while X * A < Y and X * A - X <= B:
        X *= A
        ans += 1
    ans += (Y - X - 1) // B
    print(ans)

=======
Suggestion 3

def main():
    X, Y, A, B = map(int, input().split())
    exp = 0
    while True:
        if X * A < X + B and X * A < Y:
            X *= A
            exp += 1
        else:
            exp += (Y - 1 - X) // B
            print(exp)
            return

=======
Suggestion 4

def main():
    X, Y, A, B = map(int, input().split())
    exp = 0
    while X * (A - 1) < B and X * A < Y:
        X *= A
        exp += 1
    exp += (Y - X - 1) // B
    print(exp)

=======
Suggestion 5

def main():
    X, Y, A, B = map(int, input().split())
    ans = 0
    while X * A < Y:
        if X * A - X <= B:
            ans += 1
            X *= A
        else:
            break
    ans += (Y - X - 1) // B
    print(ans)

=======
Suggestion 6

def main():
    X, Y, A, B = map(int, input().split())
    ans = 0
    while True:
        if X * A >= Y:
            break
        if X * A - X <= B:
            break
        X *= A
        ans += 1
    ans += (Y - X - 1) // B
    print(ans)

=======
Suggestion 7

def main():
    x, y, a, b = map(int, input().split())
    
    count = 0
    while True:
        if x * a >= x + b and x * a < y:
            x *= a
            count += 1
        elif x + b < y:
            x += b
            count += 1
        else:
            break
    
    print(count)

main()

=======
Suggestion 8

def main():
    X, Y, A, B = map(int, input().split())
    # X < Y
    # A >= 2
    # B >= 1
    # 1 ≦ X < Y ≦ 10^{18}
    # 2 ≦ A ≦ 10^9
    # 1 ≦ B ≦ 10^9
    # X
