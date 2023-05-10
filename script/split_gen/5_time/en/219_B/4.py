def main():
    S_1 = input()
    S_2 = input()
    S_3 = input()
    T = input()
    result = ''
    for i in range(len(T)):
        if T[i] == '1':
            result += S_1
        elif T[i] == '2':
            result += S_2
        elif T[i] == '3':
            result += S_3
    print(result)
