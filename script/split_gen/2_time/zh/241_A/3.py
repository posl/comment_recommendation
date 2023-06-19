def main():
    a = [int(x) for x in input().split()]
    b = 0
    for i in range(3):
        b = a[b]
    print(b)
