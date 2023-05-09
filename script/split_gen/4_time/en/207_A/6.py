def main():
    a = input()
    a = a.split()
    a = [int(n) for n in a]
    a = sorted(a)
    print(a[1]+a[2])
