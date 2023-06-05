Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    H = list(map(int, input().split()))
    count = 0
    for i in range(N):
        if i == 0:
            count += 1
        else:
            for j in range(i):
                if H[j] > H[i]:
                    break
                if j == i-1:
                    count += 1
    print(count)

=======
Suggestion 2

def main():
    N = int(input())
    H = list(map(int, input().split()))
    count = 0
    for i in range(N):
        flag = True
        for j in range(i):
            if H[i] < H[j]:
                flag = False
        if flag:
            count += 1
    print(count)

=======
Suggestion 3

def main():
    n = int(input())
    h = list(map(int, input().split()))
    count = 0
    for i in range(n):
        if i == 0:
            count += 1
        elif h[i] >= max(h[0:i]):
            count += 1
    print(count)

=======
Suggestion 4

def main():
    N = int(input())
    H = input().split()
    H = [int(i) for i in H]
    count = 0
    for i in range(1,N+1):
        if i == 1:
            count += 1
        else:
            flag = True
            for j in range(1,i):
                if H[j-1] > H[i-1]:
                    flag = False
            if flag:
                count += 1
    print(count)

=======
Suggestion 5

def main():
    n = int(input())
    h = list(map(int, input().split()))
    count = 1
    for i in range(1, n):
        flag = True
        for j in range(i):
            if h[j] >= h[i]:
                flag = False
                break
        if flag:
            count += 1
    print(count)

=======
Suggestion 6

def main():
    N = int(input())
    H = list(map(int, input().split()))
    cnt = 0
    max_h = 0
    for i in range(N):
        if max_h <= H[i]:
            cnt += 1
            max_h = H[i]
    print(cnt)

=======
Suggestion 7

def get_sea_view_count(mountain_list):
    """
    计算可以看到海景的旅馆数量
    :param mountain_list: 山峰高度列表
    :return: 可以看到海景的旅馆数量
    """
    # 从第一个开始遍历
    sea_view_count = 1
    # 从第二个开始遍历
    for index in range(1, len(mountain_list)):
        # 从第一个开始遍历
        for pre_index in range(0, index):
            # 判断是否可以看到海景
            if mountain_list[pre_index] > mountain_list[index]:
                # 不可以看到海景，跳出循环
                break
        else:
            # 可以看到海景，计数加1
            sea_view_count += 1
    return sea_view_count

=======
Suggestion 8

def problems124_b():
    N = int(input())
    H = list(map(int, input().split()))
    count = 0
    for i in range(N):
        flag = True
        for j in range(i):
            if H[i] < H[j]:
                flag = False
        if flag:
            count += 1
    print(count)

=======
Suggestion 9

def main():
    n = int(input())
    h = list(map(int, input().split()))
    count = 0
    for i in range(1,n+1):
        if i == 1:
            count += 1
        else:
            for j in range(1,i):
                if h[j-1] > h[i-1]:
                    break
                if j == i-1:
                    count += 1
    print(count)

=======
Suggestion 10

def get_max_index(list):
    max = list[0]
    index = 0
    for i in range(0, len(list)):
        if list[i] > max:
            max = list[i]
            index = i
    return index
