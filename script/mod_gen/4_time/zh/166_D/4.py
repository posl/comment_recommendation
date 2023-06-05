def get_a_b(x):
    for a in range(-1000,1001):
        for b in range(-1000,1001):
            if a**5 - b**5 == x:
                return a, b
x = int(input())
a, b = get_a_b(x)
print(a, b)

if __name__ == '__main__':
    get_a_b()