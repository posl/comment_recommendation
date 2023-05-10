def main():
    a = list(map(int, input().split()))
    for i in range(3):
        a = a[a[0]]
    print(a)
