Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    if s[0] == '0':
        print('No')
        return
    for i in range(9):
        if s[i] == '1' and s[i+1] == '1':
            print('Yes')
            return
    print('No')

=======
Suggestion 2

def main():
    S = input()
    if S[0] == "0":
        print("No")
        return
    for i in range(1, 10):
        if S[i] == "1":
            continue
        if S[i-1] == "1":
            print("Yes")
            return
    print("No")

=======
Suggestion 3

def main():
    S = input()
    # S = "0101110101"
    # S = "0100101001"
    # S = "0000100110"
    # S = "1101110101"
    # S = "1111111111"
    # S = "0000000000"
    # S = "0000000001"
    # S = "0000000010"
    # S = "0000000100"
    # S = "0000001000"
    # S = "0000010000"
    # S = "0000100000"
    # S = "0001000000"
    # S = "0010000000"
    # S = "0100000000"
    # S = "1000000000"
    # S = "0000000000"

    if S[0] == "1":
        print("No")
        return

    if S[-1] == "1":
        print("No")
        return

    if S[1:-1].count("1") == 0:
        print("No")
        return

    print("Yes")

=======
Suggestion 4

def main():
    S = input()
    if S[0] == "0":
        print("No")
        return
    if S[1] == "0":
        print("No")
        return
    if S[8] == "0":
        print("No")
        return
    if S[9] == "0":
        print("No")
        return
    print("Yes")
    return

=======
Suggestion 5

def main():
    S = input()
    if S[0] == '0':
        print('No')
        return
    if S[9] == '0':
        print('No')
        return
    if S[1:9].count('1') == 0:
        print('No')
        return
    print('Yes')

=======
Suggestion 6

def main():
    s = input()
    if s[0] == '0':
        print('No')
        return
    if s[1:10].count('1') == 0:
        print('No')
        return
    if s[1:10].count('0') == 0:
        print('No')
        return
    print('Yes')

=======
Suggestion 7

def main():
    s = input()
    if s[0] == "1" or s[-1] == "1":
        print("No")
        return
    s = s[1:-1]
    print("Yes" if "00" in s else "No")

=======
Suggestion 8

def main():
    s = input()
    if s[0] != '1':
        print('No')
    else:
        s = s[1:]
        if s.count('1') == 1:
            print('No')
        else:
            print('Yes')

=======
Suggestion 9

def main():
    s = input()
    # スプリットになる条件
    # 1.ピン1が倒れている
    # 2.ピン1の左右にピンが立っている
    # 3.ピン1の左右にピンが倒れている
    # 4.ピン1の左右にピンが立っている
    # 1,2,3,4の条件を満たす場合、ピン1の左右にピンが立っている
    # この場合はピン1の左右のピンが立っている列はスプリット
    if s[0] == "0" and s[1] == "1" and s[2] == "0" and s[3] == "1" and s[4] == "1" and s[5] == "0" and s[6] == "1" and s[7] == "0" and s[8] == "1" and s[9] == "0":
        print("Yes")
    else:
        print("No")

=======
Suggestion 10

def main():
    S = input()

    if S[0] == "0":
        print("No")
        return

    # 1 が立っている列の間に 0 が存在するかどうか
    for i in range(1, 9):
        if S[i] == "1" and S[i+1] == "0":
            print("No")
            return

    print("Yes")
