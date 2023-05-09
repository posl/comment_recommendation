def main():
    x = input()
    if x[-1] == '0' or x[-1] == '1' or x[-1] == '2':
        print(x[:-2] + '-')
    elif x[-1] == '3' or x[-1] == '4' or x[-1] == '5' or x[-1] == '6':
        print(x[:-2])
    else:
        print(x[:-2] + '+')
