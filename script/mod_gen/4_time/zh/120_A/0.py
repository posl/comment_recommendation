def main():
    a, b, c = map(int, input().split())
    #print(a, b, c)
    if a > c:
        print(0)
        return
    print(b//a if b//a < c else c)
main()
