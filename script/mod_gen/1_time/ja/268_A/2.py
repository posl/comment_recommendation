def main():
    # input
    As = [*map(int, input().split())]
    # compute
    As = set(As)
    # output
    print(len(As))

if __name__ == '__main__':
    main()