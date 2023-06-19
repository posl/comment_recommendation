def main():
    X, Y = map(int, input().split())
    if X % 2 != Y % 2:
        print(0)
        exit()
    if X == Y == 0:
        print(1)
        exit()
    if X == Y:
        print(2)
        exit()
    print(0)
main()
