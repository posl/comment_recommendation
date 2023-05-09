def main():
    dots = []
    for i in range(10):
        dots.append(input())
    for i in range(10):
        dots[i] = dots[i].replace('.', '0')
        dots[i] = dots[i].replace('#', '1')
        dots[i] = list(map(int, dots[i]))
    dots = list(map(list, zip(*dots)))
    for i in range(10):
        dots[i] = list(map(str, dots[i]))
        dots[i] = ''.join(dots[i])
        dots[i] = dots[i].replace('0', '.')
        dots[i] = dots[i].replace('1', '#')
    for i in range(10):
        print(dots[i])

if __name__ == '__main__':
    main()