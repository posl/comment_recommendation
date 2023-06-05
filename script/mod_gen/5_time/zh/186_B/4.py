def main():
    h,w = map(int,input().split())
    a = [list(map(int,input().split())) for _ in range(h)]
    min_a = min([min(i) for i in a])
    print(sum([sum(i) for i in a]) - min_a * h * w)

if __name__ == '__main__':
    main()