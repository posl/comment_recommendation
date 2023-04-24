Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    D = int(input())
    if D == 25:
        print("Christmas")
    elif D == 24:
        print("Christmas Eve")
    elif D == 23:
        print("Christmas Eve Eve")
    elif D == 22:
        print("Christmas Eve Eve Eve")

=======
Suggestion 2

def main():
    d = int(input())
    if d == 25:
        print("Christmas")
    elif d == 24:
        print("Christmas Eve")
    elif d == 23:
        print("Christmas Eve Eve")
    elif d == 22:
        print("Christmas Eve Eve Eve")
    else:
        print("Error")

main()

=======
Suggestion 3

def main():
    # 文字列の入力
    D = input()

    # 出力
    if D == "25":
        print("Christmas")
    elif D == "24":
        print("Christmas Eve")
    elif D == "23":
        print("Christmas Eve Eve")
    else:
        print("Christmas Eve Eve Eve")

=======
Suggestion 4

def main():
    D = int(input())
    print("Christmas" + " Eve"*(25-D))

=======
Suggestion 5

def main():
    D = int(input())
    print('Christmas' + ' Eve'*(25-D))
