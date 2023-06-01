Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    v,t,s,d = map(int,input().split())
    if v*t <= d <= v*s:
        print("No")
    else:
        print("Yes")

=======
Suggestion 2

def play_ball():
    v, t, s, d = map(int, input().split())
    if d/v >= t and d/v <= s:
        print('No')
    else:
        print('Yes')

play_ball()

=======
Suggestion 3

def main():
    v,t,s,d = map(int, input().split())
    if d < v*t or v*s < d:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    v,t,s,d = map(int, input().split())
    print("Yes" if (t * v <= d <= s * v) else "No")

=======
Suggestion 5

def main():
    v,t,s,d = map(int,input().split())
    if d < v*t or d > v*s:
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    # 读取输入
    input = raw_input()
    # 读取输入，分割成列表
    input_list = input.split(' ')
    # 把列表里的元素转换成整数
    input_list = [int(x) for x in input_list]
    # 把列表里的元素赋值给变量
    V,T,S,D = input_list
    # 计算球飞行的距离
    distance = V*T
    # 判断是否能被击中
    if distance <= D <= V*S:
        print 'No'
    else:
        print 'Yes'

=======
Suggestion 7

def main():
    v, t, s, d = map(int, input().split())
    if d / v >= t and d / v <= s:
        print("No")
    else:
        print("Yes")

=======
Suggestion 8

def main():
    v,t,s,d = map(int,input().split())
    if d < t * v or d > s * v:
        print('Yes')
    else:
        print('No')
