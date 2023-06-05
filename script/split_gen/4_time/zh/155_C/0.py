def main():
    n = int(input())
    s_list = []
    for i in range(n):
        s_list.append(input())
    s_list.sort()
    max = 0
    for i in range(n):
        if s_list.count(s_list[i]) > max:
            max = s_list.count(s_list[i])
    for i in range(n):
        if s_list.count(s_list[i]) == max:
            print(s_list[i])
