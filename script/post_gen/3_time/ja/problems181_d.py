Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    S = input()
    if "8" in S:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    s = input()
    if '8' in s:
        print('Yes')
    else:
        print('No')

=======
Suggestion 3

def main():
    S = input()
    if '8' in S:
        print('Yes')
    else:
        print('No')

=======
Suggestion 4

def main():
    s = input()
    if s.count("8") > 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def main():
    S = input()
    if '8' in S:
        if int(S) % 8 == 0:
            print('Yes')
        else:
            if int(S[1:]) % 8 == 0:
                print('Yes')
            else:
                if int(S[1:]+S[0]) % 8 == 0:
                    print('Yes')
                else:
                    print('No')
    else:
        print('No')

=======
Suggestion 6

def main():
    s = input()
    if '0' in s:
        print('Yes')
        return
    if len(s) < 3:
        print('No')
        return
    l = []
    for i in range(len(s)):
        l.append(int(s[i]))
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            for k in range(j+1, len(l)):
                if (l[i]*100 + l[j]*10 + l[k]) % 8 == 0:
                    print('Yes')
                    return
    print('No')

=======
Suggestion 7

def main():
    S = input()
    S = sorted(S)
    if S[0] != "0":
        print("No")
        return
    if S.count("0") == len(S):
        print("Yes")
        return
    if len(S) < 3:
        print("No")
        return
    for i in range(1, len(S)):
        for j in range(i+1, len(S)):
            if (int(S[i])*10+int(S[j])) % 8 == 0:
                print("Yes")
                return
            if (int(S[i])*10+int(S[j])) % 8 == 0:
                print("Yes")
                return
    print("No")

=======
Suggestion 8

def main():
    # 入力
    S = input()

    # 8の倍数を作れるかどうか
    flag = False

    # 8の倍数を作れるかどうか判定
    if "8" in S:
        flag = True
    elif "0" in S:
        flag = True
    elif "7" in S:
        flag = True
    elif "6" in S:
        flag = True
    elif "5" in S:
        flag = True
    elif "4" in S:
        flag = True
    elif "3" in S:
        flag = True
    elif "2" in S:
        flag = True
    elif "1" in S:
        flag = True
    else:
        flag = False

    # 出力
    if flag:
        print("Yes")
    else:
        print("No")

=======
Suggestion 9

def main():
    S = input()
    N = len(S)
    # 8の倍数を作れるか作れないかを判定する
    # 8の倍数を作るためには、8で割った余りが0である必要がある
    # 8で割った余りが0となる数は、8, 16, 24, ... となる
    # 8で割った余りが0となる数を作るためには、
    # 8の倍数である必要があり、8の倍数であるためには、
    # 8の倍数を作るためには、8で割った余りが0である必要がある
    # つまり、8の倍数を作るためには、8で割った余りが0である必要がある
    # 8で割った余りが0となる数は、8, 16, 24, ... となる
    # 8で割った余りが0となる数を作るためには、
    # 8の倍数である必要があり、8の倍数であるためには、
    # 8の倍数を作るためには、8で割った余りが0である必要がある
    # つまり、8の倍数を作るためには、8で割った余りが0である必要がある
    # 8で割った余りが0となる数は、8, 16, 24, ... となる
    # 8で割った余りが0となる数を作るためには、
    # 8の倍数である必要があり、8の倍数であるためには、
    # 8の倍数を作るためには、8で割った余りが0
