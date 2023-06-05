def main():
    s = input()
    t = input()
    s_sort = sorted(s)
    t_sort = sorted(t)
    if s_sort == t_sort:
        print("Yes")
    else:
        print("No")
