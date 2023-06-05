def main():
    a, b, c, d, e = map(int, input().split())
    A = [a, b, c, d, e]
    print(len(set(A)))
main()
