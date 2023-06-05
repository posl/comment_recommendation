def problem248_a():
    s = input()
    s = sorted(s)
    for i in range(10):
        if s[i] != str(i):
            print(i)
            break

if __name__ == '__main__':
    problem248_a()