def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(input())
    a.reverse()
    for i in range(n):
        print(a[i])
