def main():
    a, b = map(int, input().split())
    print("{:.3f}".format(round(b/a, 3)))
main()

if __name__ == '__main__':
    main()