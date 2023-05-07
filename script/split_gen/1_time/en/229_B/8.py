def main():
    A, B = map(int, input().split())
    print('Easy' if (A+B) < 10 else 'Hard')
