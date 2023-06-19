def main():
    s_1 = input()
    s_2 = input()
    s_3 = input()
    t = input()
    result = ""
    for i in t:
        if i == "1":
            result += s_1
        elif i == "2":
            result += s_2
        else:
            result += s_3
    print(result)
main()
