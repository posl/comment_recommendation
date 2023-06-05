def main():
    a = input()
    a = a.split()
    b = 0
    for i in range(3):
        b = a[b]
        b = int(b)
    print(b)
