def main():
    a = input().split()
    a = [int(i) for i in a]
    for i in range(3):
        a = [a[j] for j in a]
    print(a[0])
