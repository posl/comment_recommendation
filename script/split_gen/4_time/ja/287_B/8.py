def main():
    n,m = map(int,input().split())
    s_list = [input() for i in range(n)]
    t_list = [input() for i in range(m)]
    count = 0
    for s in s_list:
        for t in t_list:
            if s[-3:] == t:
                count += 1
    print(count)
