def main():
    a = [int(x) for x in input().split()]
    x = 0
    for i in range(3):
        x = a[x]
    print(x)
