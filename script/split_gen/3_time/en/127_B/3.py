def main():
    r, D, x_2000 = map(int, input().split())
    for i in range(10):
        x_2000 = r*x_2000 - D
        print(x_2000)
