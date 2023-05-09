def rank(n):
    if n >= 90:
        return "expert"
    elif n >= 70:
        return 90 - n
    elif n >= 40:
        return 70 - n
    else:
        return 40 - n
n = int(input())
print(rank(n))

if __name__ == '__main__':
    rank()