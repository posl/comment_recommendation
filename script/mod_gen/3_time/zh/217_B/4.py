def find_missing_element(list):
    for i in range(len(list)):
        if list[i] == "ABC":
            list.remove("ABC")
        elif list[i] == "ARC":
            list.remove("ARC")
        elif list[i] == "AGC":
            list.remove("AGC")
        elif list[i] == "AHC":
            list.remove("AHC")
    return list

if __name__ == '__main__':
    find_missing_element()