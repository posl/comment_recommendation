def main():
    a, b, w = map(int, input().split())
    w *= 1000
    min_oranges = w // b
    max_oranges = w // a
    if w % b != 0:
        min_oranges += 1
    if w % a != 0:
        max_oranges -= 1
    if min_oranges > max_oranges:
        print('UNSATISFIABLE')
    else:
        print(min_oranges, max_oranges)

if __name__ == '__main__':
    main()