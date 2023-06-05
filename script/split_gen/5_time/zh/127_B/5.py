def main():
    # r D x_2000
    r, D, x = map(int, input().split())
    for i in range(10):
        x = r * x - D
        print(x)
