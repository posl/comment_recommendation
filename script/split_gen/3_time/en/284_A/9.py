def main():
    n = int(input())
    print('
'.join([input() for i in range(n)][::-1]))
