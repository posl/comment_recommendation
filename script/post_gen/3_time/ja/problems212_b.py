Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    X = input()
    if X[0] == X[1] and X[1] == X[2] and X[2] == X[3]:
        print("Weak")
    elif int(X[0]) + 1 == int(X[1]) and int(X[1]) + 1 == int(X[2]) and int(X[2]) + 1 == int(X[3]):
        print("Weak")
    elif int(X[0]) == 9 and int(X[1]) == 0 and int(X[2]) == 1 and int(X[3]) == 2:
        print("Weak")
    else:
        print("Strong")

=======
Suggestion 2

def main():
    X = input()
    if X[0] == X[1] and X[1] == X[2] and X[2] == X[3]:
        print("Weak")
    elif int(X[0]) + 1 == int(X[1]) and int(X[1]) + 1 == int(X[2]) and int(X[2]) + 1 == int(X[3]):
        print("Weak")
    elif X[0] == "9" and X[1] == "0" and X[2] == "1" and X[3] == "2":
        print("Weak")
    else:
        print("Strong")

=======
Suggestion 3

def main():
    X = input()
    if X[0] == X[1] == X[2] == X[3] or (int(X[0]) + 1) % 10 == int(X[1]) and (int(X[1]) + 1) % 10 == int(X[2]) and (int(X[2]) + 1) % 10 == int(X[3]):
        print("Weak")
    else:
        print("Strong")

=======
Suggestion 4

def main():
    X = input()
    if X[0] == X[1] == X[2] == X[3]:
        print("Weak")
    elif X[0] == X[1] and X[1] == X[2] and X[2] == str(int(X[3]) - 1):
        print("Weak")
    elif X[0] == X[1] and X[1] == str(int(X[2]) - 1) and X[2] == str(int(X[3]) - 1):
        print("Weak")
    elif X[0] == str(int(X[1]) - 1) and X[1] == str(int(X[2]) - 1) and X[2] == str(int(X[3]) - 1):
        print("Weak")
    else:
        print("Strong")

=======
Suggestion 5

def main():
    s = input()
    if s[0] == s[1] == s[2] == s[3]:
        print('Weak')
    elif int(s[0]) == (int(s[1]) - 1) % 10 and int(s[1]) == (int(s[2]) - 1) % 10 and int(s[2]) == (int(s[3]) - 1) % 10:
        print('Weak')
    else:
        print('Strong')

=======
Suggestion 6

def main():
    X = input()
    if X[0] == X[1] == X[2] == X[3]:
        print('Weak')
    elif int(X[0]) == (int(X[1]) + 1) % 10 and int(X[1]) == (int(X[2]) + 1) % 10 and int(X[2]) == (int(X[3]) + 1) % 10:
        print('Weak')
    else:
        print('Strong')

=======
Suggestion 7

def main():
    num = input()
    if num[0] == num[1] == num[2] == num[3]:
        print("Weak")
    elif num[0] == num[1] == num[2] or num[1] == num[2] == num[3]:
        print("Weak")
    elif num[0] == str(int(num[1]) - 1) == str(int(num[2]) - 2) == str(int(num[3]) - 3):
        print("Weak")
    elif num[0] == str(int(num[1]) - 1) == str(int(num[2]) - 2) == str(int(num[3]) + 7):
        print("Weak")
    else:
        print("Strong")

=======
Suggestion 8

def main():
    X = input()
    if X[0] == X[1] == X[2] == X[3]:
        print('Weak')
        exit()
    if (int(X[0]) + 1) % 10 == int(X[1]) and (int(X[1]) + 1) % 10 == int(X[2]) and (int(X[2]) + 1) % 10 == int(X[3]):
        print('Weak')
        exit()
    print('Strong')

=======
Suggestion 9

def main():
    X = input()
    X = list(map(int, X))
    if X[0] == X[1] == X[2] == X[3]:
        print("Weak")
        return
    if X[0] == 9 and X[1] == 0:
        if X[2] == 1 and X[3] == 2:
            print("Weak")
            return
    if X[0]+1 == X[1] and X[1]+1 == X[2] and X[2]+1 == X[3]:
        print("Weak")
        return
    print("Strong")
    return

=======
Suggestion 10

def main():
    # 標準入力から暗証番号を取得
    passcode = input()

    # 暗証番号の4桁がすべて同じ数字の場合、弱い暗証番号とする
    if passcode[0] == passcode[1] and passcode[1] == passcode[2] and passcode[2] == passcode[3]:
        print("Weak")
        return

    # 暗証番号の4桁が連続している場合、弱い暗証番号とする
    if passcode[1] == str(int(passcode[0]) + 1) and passcode[2] == str(int(passcode[1]) + 1) and passcode[3] == str(int(passcode[2]) + 1):
        print("Weak")
        return

    # 暗証番号の4桁が連続している場合、弱い暗証番号とする
    if passcode[0] == "9" and passcode[1] == "0" and passcode[2] == "1" and passcode[3] == "2":
        print("Weak")
        return

    # どちらにも該当しない場合、強い暗証番号とする
    print("Strong")
    return
