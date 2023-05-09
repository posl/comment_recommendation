def f(x):
    divs = 0
    for i in range(1, x+1):
        if x%i == 0:
            divs += 1
    return divs
n = int(input())
total = 0
for i in range(1, n+1):
    total += i*f(i)
print(total)

if __name__ == '__main__':
    f()