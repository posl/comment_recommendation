def main():
    n = int(input())
    q_list = []
    for i in range(n):
        q_list.append(list(map(int, input().split())))
    s = []
    for i in range(n):
        if q_list[i][0] == 1:
            s.append(q_list[i][1])
        elif q_list[i][0] == 2:
            for j in range(q_list[i][2]):
                if q_list[i][1] in s:
                    s.remove(q_list[i][1])
        else:
            s.sort()
            print(s[-1]-s[0])
