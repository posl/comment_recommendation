def problem191_a():
    v, t, s, d = map(int, input().split())
    if d < v * t or d > v * s:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    problem191_a()