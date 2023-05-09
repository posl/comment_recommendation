def main():
    #入力
    S1 = input()
    S2 = input()
    S3 = input()
    T = input()
    #出力
    for i in range(len(T)):
        if T[i] == '1':
            print(S1, end='')
        elif T[i] == '2':
            print(S2, end='')
        elif T[i] == '3':
            print(S3, end='')
        else:
            print('error')
            break
