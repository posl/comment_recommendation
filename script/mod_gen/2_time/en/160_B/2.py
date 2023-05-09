def get_happiness(x):
    happiness = 0
    happiness += (x // 500) * 1000
    x = x % 500
    happiness += (x // 5) * 5
    return happiness
x = int(input())
print(get_happiness(x))

if __name__ == '__main__':
    get_happiness()