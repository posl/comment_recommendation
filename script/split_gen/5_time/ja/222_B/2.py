def main():
    n, p = map(int, input().split())
    a = list(map(int, input().split()))
    print(len(list(filter(lambda x: x < p, a))))
