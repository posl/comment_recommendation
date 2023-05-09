def main():
    N, X = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(N)]
    for (a, b) in ab:
        if X >= a and X <= b:
            print("Yes")
            exit()
    print("No")
