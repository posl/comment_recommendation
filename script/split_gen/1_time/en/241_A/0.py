def main():
    a = list(map(int, input().split()))
    for i in range(3):
        a = [a[a[i]] for i in range(10)]
    print(a[0])
