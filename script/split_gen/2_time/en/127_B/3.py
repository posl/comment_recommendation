def main():
    r, D, x2000 = map(int, input().split())
    for i in range(2000, 2010):
        x = r * x2000 - D
        print(x)
        x2000 = x
