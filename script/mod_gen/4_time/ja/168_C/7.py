def main():
    A, B, H, M = map(int, input().split())
    import math
    pi = math.pi
    #print(pi)
    #print(A, B, H, M)
    #print(2 * pi / 12 * H)
    #print(2 * pi / 60 * M)
    #print(2 * pi / 12 * H + 2 * pi / 60 * M)
    #print(abs(2 * pi / 12 * H - 2 * pi / 60 * M))
    #print(math.cos(abs(2 * pi / 12 * H - 2 * pi / 60 * M)))
    print(math.sqrt(A ** 2 + B ** 2 - 2 * A * B * math.cos(abs(2 * pi / 12 * H - 2 * pi / 60 * M))))

if __name__ == '__main__':
    main()