def main():
    a = input().split()
    for i in range(len(a)):
        a[i] = int(a[i])
    print(min(a))
