def main():
    l, q = map(int, input().split())
    l_list = [l]
    for _ in range(q):
        c, x = map(int, input().split())
        if c == 1:
            for i, l_i in enumerate(l_list):
                if l_i > x:
                    l_list[i] = x
                    l_list.insert(i + 1, l_i - x)
                    break
        else:
            for l_i in l_list:
                if l_i >= x:
                    print(l_i)
                    break
