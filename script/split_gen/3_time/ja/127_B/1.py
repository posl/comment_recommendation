def main():
    r, D, x2000 = map(int, input().split())
    x = x2000
    for i in range(10):
        x = r * x - D
        print(x)
