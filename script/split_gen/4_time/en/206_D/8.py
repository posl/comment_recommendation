def main():
    n = int(input())
    a = list(map(int, input().split()))
    a_set = set(a)
    a_set = list(a_set)
    a_set.sort()
    a_set.reverse()
    a_set_len = len(a_set)
    if a_set_len == 1:
        print(0)
    elif a_set_len == 2:
        if a_set[0] == 0:
            print(0)
        else:
            print(1)
    elif a_set_len == 3:
        if a_set[0] == a_set[1] == a_set[2]:
            print(0)
        elif a_set[0] == a_set[1] or a_set[1] == a_set[2]:
            print(1)
        else:
            print(2)
    else:
        if a_set[0] == a_set[1] == a_set[2] == a_set[3]:
            print(0)
        elif a_set[0] == a_set[1] == a_set[2]:
            print(1)
        elif a_set[0] == a_set[1] and a_set[2] == a_set[3]:
            print(1)
        elif a_set[0] == a_set[1]:
            print(2)
        elif a_set[1] == a_set[2] == a_set[3]:
            print(2)
        else:
            print(3)
