def main():
    X = input()
    if X[2] == '0' or X[2] == '1' or X[2] == '2':
        print(X[0:2] + '-')
    elif X[2] == '3' or X[2] == '4' or X[2] == '5' or X[2] == '6':
        print(X[0:2])
    elif X[2] == '7' or X[2] == '8' or X[2] == '9':
        print(X[0:2] + '+')
