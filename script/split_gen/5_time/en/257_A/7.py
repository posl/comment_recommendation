def problem257_a():
    n, x = map(int, input().split())
    print(chr(x-1+ord('A')*(x-1)//n))
