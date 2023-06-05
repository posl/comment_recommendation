def p193_a():
    a, b = map(int, input().split())
    print("{:.20f}".format(100*(a-b)/a))
