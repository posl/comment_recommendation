def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append([int(x) for x in input().split()])
    print(a)
