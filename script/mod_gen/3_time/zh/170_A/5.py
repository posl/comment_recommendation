def problems170_a():
    x = input().split()
    for i in range(len(x)):
        if x[i] == '0':
            print(i+1)
            break

if __name__ == '__main__':
    problems170_a()