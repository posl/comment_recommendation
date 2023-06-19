def main():
    A, B, W = map(int, input().split())
    W *= 1000
    min = W // B
    max = W // A
    if min * B == W:
        print(min, max)
    elif max * A <= W:
        print(min + 1, max)
    else:
        print('UNSATISFIABLE')
main()
