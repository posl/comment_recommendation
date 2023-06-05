def problems257_a():
    #N, X = map(int, input().split())
    N, X = 2, 12
    if N < 1 or N > 100 or X < 1 or X > N*26:
        return
    print(chr(ord('A') + (X - 1) % 26))
