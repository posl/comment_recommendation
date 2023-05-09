def main():
    n = int(input())
    seq = [1]
    for i in range(1, n):
        seq = seq + [i + 1] + seq
    print(" ".join(str(x) for x in seq))

if __name__ == '__main__':
    main()