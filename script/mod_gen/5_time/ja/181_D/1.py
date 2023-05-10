def get_yes_or_no(s):
    s_list = list(s)
    for i in range(0, len(s_list)):
        for j in range(i+1, len(s_list)):
            for k in range(j+1, len(s_list)):
                num = int(s_list[i] + s_list[j] + s_list[k])
                if num % 8 == 0:
                    return "Yes"
    return "No"

if __name__ == '__main__':
    get_yes_or_no()