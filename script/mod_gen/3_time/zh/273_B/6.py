def problem273_b(x, k):
    for i in range(k):
        x = int((x+5)/10)*10
    print(x)

if __name__ == '__main__':
    problem273_b()