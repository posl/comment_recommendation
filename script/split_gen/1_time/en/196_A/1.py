def main():
    a, b = [int(x) for x in input().split()]
    c, d = [int(x) for x in input().split()]
    print(max(abs(a-c), abs(a-d), abs(b-c), abs(b-d)))
main()
