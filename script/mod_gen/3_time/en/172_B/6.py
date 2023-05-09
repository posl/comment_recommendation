def main():
    s = input()
    t = input()
    print(sum(1 for x, y in zip(s, t) if x != y))

if __name__ == '__main__':
    main()