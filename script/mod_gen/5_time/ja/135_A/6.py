def main():
    a, b = map(int, input().split())
    if a < b:
        print(b - (b - a) // 2)
    else:
        print(a - (a - b) // 2)
main()
