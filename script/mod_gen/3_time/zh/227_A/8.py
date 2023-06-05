def problem227_a(n,k,a):
    #n个人，k张卡片，第一个人a
    if a == 1:
        return k%n
    else:
        return (k+a-1)%n

if __name__ == '__main__':
    problem227_a()