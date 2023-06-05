def main():
    a = list(map(int, input().split()))
    b = [0] * 10
    for i in range(10):
        b[a[i]] = i
    for i in range(3):
        b = [b[a[i]] for i in range(10)]
    print(b[0])
