def main():
    s = input()
    #print(s)
    #print(len(s))
    if len(s) < 2 or len(s) > 100:
        print("No")
        return
    if s.islower():
        print("No")
        return
    if s.isupper():
        print("No")
        return
    if s.isalpha() == False:
        print("No")
        return
    if s.isalnum() == False:
        print("No")
        return
    if s.isnumeric() == True:
        print("No")
        return
    if s.isdecimal() == True:
        print("No")
        return
    if s.isidentifier() == True:
        print("No")
        return
    if s.isprintable() == False:
        print("No")
        return
    if s.isspace() == True:
        print("No")
        return
    if s.istitle() == True:
        print("No")
        return
    if s.isascii() == False:
        print("No")
        return
    if s.islower() == False and s.isupper() == False:
        print("Yes")
        return
    print("No")
    return
main()
# AC
# 1m AC
