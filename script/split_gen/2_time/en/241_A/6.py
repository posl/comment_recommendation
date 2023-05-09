def main():
    a = input().split()
    current = 0
    for i in range(3):
        current = int(a[current])
    print(current)
