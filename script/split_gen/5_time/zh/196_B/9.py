def main():
    x = input()
    if x.find('.') == -1:
        print(x)
    else:
        x = x.split('.')
        if int(x[1][0]) >= 5:
            print(int(x[0]) + 1)
        else:
            print(int(x[0]))
