def main():
    a, b = list(map(int, input().strip().split()))
    print('{:.3f}'.format(round(b/a, 4)))
