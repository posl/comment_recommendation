def main():
    a = list(map(int, input().split()))
    b = 0
    for i in range(3):
        b = a[b]
    print(b)
