def concatenate_strings(S_1, S_2, S_3, T):
    if len(S_1) <= 10 and len(S_2) <= 10 and len(S_3) <= 10 and len(T) <= 1000:
        if T.count("1") + T.count("2") + T.count("3") == len(T):
            result = ""
            for i in T:
                if i == "1":
                    result += S_1
                elif i == "2":
                    result += S_2
                elif i == "3":
                    result += S_3
            print(result)

if __name__ == '__main__':
    concatenate_strings()