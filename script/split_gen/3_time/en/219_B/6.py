def main():
    S_1 = input()
    S_2 = input()
    S_3 = input()
    T = input()
    for i in range(len(T)):
        if T[i] == '1':
            print(S_1, end='')
        elif T[i] == '2':
            print(S_2, end='')
        elif T[i] == '3':
            print(S_3, end='')
