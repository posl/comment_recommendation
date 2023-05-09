def main():
    n = int(input())
    s = [input() for _ in range(n)]
    s_set = set(s)
    s_dict = {key:0 for key in s_set}
    for i in s:
        s_dict[i] += 1
    s_dict = sorted(s_dict.items(), key=lambda x: -x[1])
    max_val = s_dict[0][1]
    for i in range(len(s_dict)):
        if s_dict[i][1] == max_val:
            print(s_dict[i][0])
        else:
            break
