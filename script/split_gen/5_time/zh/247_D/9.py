def main():
    q = int(input())
    for i in range(q):
        a = input().split()
        if a[0] == "1":
            print(a[1], a[2])
