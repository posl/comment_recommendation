def main():
    h, w = map(int, input().split())
    a = [input() for _ in range(h)]
    a = [row for row in a if '#' in row]
    a = list(zip(*[row for row in zip(*a) if '#' in row]))
    print('\n'.join(''.join(row) for row in a))

if __name__ == '__main__':
    main()