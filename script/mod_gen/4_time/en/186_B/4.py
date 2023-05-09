def main():
    h, w = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    print(sum([sum(x) for x in a]) - min([min(x) for x in a]) * h * w)

if __name__ == '__main__':
    main()