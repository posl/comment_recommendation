def main():
    # input
    S_1 = input()
    S_2 = input()
    S_3 = input()
    S_4 = input()
    # compute
    S_list = [S_1, S_2, S_3, S_4]
    if (S_list.count("H") == 1) and (S_list.count("2B") == 1) and (S_list.count("3B") == 1) and (S_list.count("HR") == 1):
        result = "Yes"
    else:
        result = "No"
    # output
    print(result)
