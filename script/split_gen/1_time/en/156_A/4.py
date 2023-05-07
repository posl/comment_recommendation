def main():
    N, R = [int(x) for x in input().split()]
    if N >= 10:
        print(R)
    else:
        print(R + 100 * (10 - N))
