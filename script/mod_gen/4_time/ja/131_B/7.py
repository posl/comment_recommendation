def apple_pie(n, l):
    taste = []
    for i in range(n):
        taste.append(l+i)
    taste.sort()
    return sum(taste[1:])

if __name__ == '__main__':
    apple_pie()