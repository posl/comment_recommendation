def abc109_a():
    a, b = map(int, input().split())
    print('Yes' if (a*b)%2==1 else 'No')
abc109_a()

if __name__ == '__main__':
    abc109_a()