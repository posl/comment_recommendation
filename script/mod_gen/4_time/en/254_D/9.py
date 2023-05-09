def problem254_d():
    n = int(input())
    # print(n)
    # print(int(n**0.5))
    # print(int(n**0.5) * int(n**0.5))
    # print(int(n**0.5) * int(n**0.5) == n)
    count = 0
    for i in range(1, int(n**0.5)+1):
        for j in range(1, int(n**0.5)+1):
            # print(i, j)
            if i * j <= n and i * j == int(i * j):
                count += 1
    print(count)

if __name__ == '__main__':
    problem254_d()