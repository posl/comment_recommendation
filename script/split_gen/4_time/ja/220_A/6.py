def main():
    a, b, c = map(int, input().split())
    if a % c == 0:
        print(a)
    else:
        print(a + c - (a % c))
