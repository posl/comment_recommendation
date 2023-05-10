def icecream():
    a, b = map(int, input().split())
    if a+b >= 15 and b >= 8:
        return 1
    if a+b >= 10 and b >= 3:
        return 2
    if a+b >= 3:
        return 3
    return 4
print(icecream())

if __name__ == '__main__':
    icecream()