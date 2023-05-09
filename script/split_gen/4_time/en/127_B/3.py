def main():
    r, D, x2000 = map(int, input().split())
    for i in range(2001, 2011):
        x2000 = r * x2000 - D
        print(x2000)
