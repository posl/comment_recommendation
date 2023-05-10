def is_arithmetic_sequence(a):
    if a[2]-a[1]==a[1]-a[0]:
        return True
    else:
        return False
a = list(map(int, input().split()))

if __name__ == '__main__':
    is_arithmetic_sequence()