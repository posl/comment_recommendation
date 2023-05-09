def problems219_a():
    x = int(input())
    if 0 <= x and x < 40:
        print(40 - x)
    elif 40 <= x and x < 70:
        print(70 - x)
    elif 70 <= x and x < 90:
        print(90 - x)
    elif 90 <= x and x <= 100:
        print('expert')
    else:
        print('error')

if __name__ == '__main__':
    problems219_a()