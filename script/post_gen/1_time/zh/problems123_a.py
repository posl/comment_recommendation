Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    k = int(input())
    if (e - a) > k:
        print(":(")
    else:
        print("Yay!")

=======
Suggestion 2

def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    k = int(input())

    if e - a > k:
        print(':(')
    else:
        print('Yay!')

=======
Suggestion 3

def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    k = int(input())
    if e - a <= k:
        print('Yay!')
    else:
        print(':(')

=======
Suggestion 4

def main():
    # 读取输入
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    k = int(input())
    # 检查是否存在一对不能直接通信的天线
    if e - a > k:
        print(":(")
    else:
        print("Yay!")

=======
Suggestion 5

def main():
    antennas = []
    # 读取输入
    for i in range(6):
        antennas.append(int(input()))
    # print(antennas)
    # 处理
    for i in range(5):
        for j in range(i + 1, 5):
            if antennas[j] - antennas[i] > antennas[5]:
                print(":(")
                return
    print("Yay!")
