def main():
    a = raw_input().split(' ')
    a = map(int, a)
    b = a[0]
    for i in range(1, 11):
        b = a[b]
    print b
