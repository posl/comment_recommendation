def problem261_c():
    n = int(input())
    names = []
    for i in range(n):
        names.append(input())
    for i in range(n):
        if names.count(names[i]) == 1:
            print(names[i])
        else:
            print(names[i]+"("+str(names[0:i].count(names[i]))+")")

if __name__ == '__main__':
    problem261_c()