def main():
    N = int(input())
    S = [tuple(map(int, input().split())) for _ in range(N)]
    T = [tuple(map(int, input().split())) for _ in range(N)]
    def rotate(p):
        return [(x * cos(p) - y * sin(p), x * sin(p) + y * cos(p)) for x, y in S]
    def translate(q, r):
        return [(x + q, y + r) for x, y in S]
    def match(S, T):
        return sorted(S) == sorted(T)
    for p in range(1, 360):
        if match(rotate(p), T):
            print("Yes")
            break
    else:
        for q in range(-10, 10):
            for r in range(-10, 10):
                if match(translate(q, r), T):
                    print("Yes")
                    break
            else:
                continue
            break
        else:
            print("No")

if __name__ == '__main__':
    main()