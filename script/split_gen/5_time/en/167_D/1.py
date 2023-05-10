def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    town = 1
    for i in range(k):
        town = a[town-1]
    print(town)
