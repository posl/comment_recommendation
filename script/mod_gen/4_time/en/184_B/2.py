def main():
    n, x = map(int, input().split())
    s = input()
    points = x
    for i in range(n):
        if s[i] == 'o':
            points += 1
        else:
            if points > 0:
                points -= 1
    print(points)

if __name__ == '__main__':
    main()