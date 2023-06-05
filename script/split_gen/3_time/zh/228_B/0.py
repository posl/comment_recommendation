def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    a = list(map(lambda x: x-1, a))
    print(len(set(a) | {x-1}))
    return
