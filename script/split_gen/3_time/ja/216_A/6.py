def main():
    x = input()
    if x[2] == '0' or x[2] == '1' or x[2] == '2':
        print(x[0:2]+'-')
    elif x[2] == '3' or x[2] == '4' or x[2] == '5' or x[2] == '6':
        print(x[0:2])
    elif x[2] == '7' or x[2] == '8' or x[2] == '9':
        print(x[0:2]+'+')
