def main():
    s = input()
    i = 0
    while i < len(s):
        if s[i].isupper():
            if i + 1 < len(s):
                if s[i + 1].isdigit():
                    if i + 6 < len(s):
                        if s[i + 6].isupper():
                            i += 7
                        else:
                            print("No")
                            return
                    else:
                        print("No")
                        return
                else:
                    i += 1
            else:
                print("No")
                return
        else:
            print("No")
            return
    print("Yes")
