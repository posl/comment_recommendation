def main():
    a = input().split()
    a = list(map(int, a))
    a.sort()
    print(a[2] - a[0])
