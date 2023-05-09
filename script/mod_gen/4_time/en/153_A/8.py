def monster():
    h, a = map(int, input().split())
    return (h + a - 1) // a
print(monster())

if __name__ == '__main__':
    monster()