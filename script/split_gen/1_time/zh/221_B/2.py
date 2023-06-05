def main():
    s = input()
    t = input()
    if len(s) == len(t):
        s_list = list(s)
        t_list = list(t)
        if s_list == t_list:
            print('Yes')
        else:
            for i in range(len(s_list)):
                for j in range(len(s_list)):
                    if i == j:
                        continue
                    else:
                        s_list[i],s_list[j] = s_list[j],s_list[i]
                        if s_list == t_list:
                            print('Yes')
                            break
                        else:
                            s_list[i],s_list[j] = s_list[j],s_list[i]
                else:
                    continue
                break
            else:
                print('No')
    else:
        print('No')
