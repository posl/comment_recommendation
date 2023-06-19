def main():
    s = input()
    if len(s) != 4:
        print("No")
        return
    else:
        for i in s:
            if s.count(i) != 2:
                print("No")
                return
        print("Yes")
