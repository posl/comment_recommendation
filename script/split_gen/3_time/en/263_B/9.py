def main():
    n = int(input())
    p = list(map(int, input().split()))
    p.insert(0, None)
    print(get_generation(n, p))
