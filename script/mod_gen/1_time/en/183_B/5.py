def f(x):
    return (Gy - Sy) / (Gx - Sx) * x + (Sx * Gy - Sy * Gx) / (Sx - Gx)
Sx, Sy, Gx, Gy = map(int, input().split())
print(f(0))

if __name__ == '__main__':
    f()