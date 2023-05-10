def f(x):
    if x == 1:
        return 1
    else:
        return 2 * f(x//2) + 1
H = int(input())
print(f(H))

if __name__ == '__main__':
    f()