Synthesizing 10/10 solutions (Duplicates hidden)

=======

def main():
    A, B, C = map(int, input().split())
    print(max(A+B+C, A+B*C, A*B+C, A*B*C, (A+B)*C, A*(B+C)))

=======

def main():
    A, B, C = map(int, input().split())
    print(max(A + B + C, A * B * C, (A + B) * C, A * (B + C)))

=======

def main():
    a, b, c = map(int, input().split())
    ans = 0
    ans = max(ans, a + b + c)
    ans = max(ans, a + b * c)
    ans = max(ans, a * b + c)
    ans = max(ans, a * b * c)
    print(ans)

=======

def main():
    A, B, C = map(int, input().split())
    print(max(A + B + C, A * B * C, A * (B + C), (A + B) * C, A + B * C, A * B + C))

=======

def main():
    A, B, C = map(int, input().split())
    print(max([A+B+C, A+B*C, A*B+C, A*B*C, (A+B)*C, A*(B+C)]))

=======

def main():
    A, B, C = map(int, input().split())
    print(max(A + B + C, A + B * C, A * (B + C), A * B * C))

=======

def main():
    a, b, c = map(int, input().split())
    ans = 0
    for op1 in ['+', '-']:
        for op2 in ['+', '-']:
            for op3 in ['+', '-']:
                if op1 == '+':
                    if op2 == '+':
                        if op3 == '+':
                            ans = max(ans, a + b + c)
                        else:
                            ans = max(ans, a + b - c)
                    else:
                        if op3 == '+':
                            ans = max(ans, a - b + c)
                        else:
                            ans = max(ans, a - b - c)
                else:
                    if op2 == '+':
                        if op3 == '+':
                            ans = max(ans, a + b + c)
                        else:
                            ans = max(ans, a + b - c)
                    else:
                        if op3 == '+':
                            ans = max(ans, a - b + c)
                        else:
                            ans = max(ans, a - b - c)
    print(ans)

=======

def main():
    A, B, C = map(int, input().split())

    max = 0

    if A + B + C > max:
        max = A + B + C

    if A + B * C > max:
        max = A + B * C

    if A * B + C > max:
        max = A * B + C

    if A * B * C > max:
        max = A * B * C

    if (A + B) * C > max:
        max = (A + B) * C

    if A * (B + C) > max:
        max = A * (B + C)

    print(max)
