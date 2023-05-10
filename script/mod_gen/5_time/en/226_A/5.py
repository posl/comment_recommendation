def rounder(x):
    if x < 0.5:
        return 0
    else:
        return 1
x = float(input())
print(round(x))

if __name__ == '__main__':
    rounder()