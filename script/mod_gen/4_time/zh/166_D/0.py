def problem166_d(x):
    for a in range(-120, 120):
        for b in range(-120, 120):
            if a ** 5 - b ** 5 == x:
                return a, b
    return 0, 0
x = int(input())
a, b = problem166_d(x)
print(a, b)

if __name__ == '__main__':
    problem166_d()