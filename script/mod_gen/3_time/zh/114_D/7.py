def problem114_d():
    n = int(input())
    count = 0
    for i in range(1,n+1):
        if n%i == 0:
            if i%75 == 0:
                count += 1
    print(count)

if __name__ == '__main__':
    problem114_d()