def main():
    s = input()
    count = 0
    for i in range(10000):
        i = str(i).zfill(4)
        if (s[0] == "o" and i[0] != "0") or (s[0] == "?" and i[0] != "0"):
            if (s[1] == "o" and i[1] != "0") or (s[1] == "?" and i[1] != "0"):
                if (s[2] == "o" and i[2] != "0") or (s[2] == "?" and i[2] != "0"):
                    if (s[3] == "o" and i[3] != "0") or (s[3] == "?" and i[3] != "0"):
                        if (s[4] == "o" and i[0] != "0") or (s[4] == "?" and i[0] != "0"):
                            if (s[5] == "o" and i[1] != "0") or (s[5] == "?" and i[1] != "0"):
                                if (s[6] == "o" and i[2] != "0") or (s[6] == "?" and i[2] != "0"):
                                    if (s[7] == "o" and i[3] != "0") or (s[7] == "?" and i[3] != "0"):
                                        if (s[8] == "o" and i[0] != "0") or (s[8] == "?" and i[0] != "0"):
                                            if (s[9] == "o" and i[1] != "0") or (s[9] == "?" and i[1] != "0"):
                                                count += 1
    print(count)

if __name__ == '__main__':
    main()