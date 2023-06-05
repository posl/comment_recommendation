def main():
    s = input()
    #print(s)
    #print(s.islower())
    #print(s.isupper())
    #print(s.isalpha())
    #print(s.isalnum())
    #print(s.isdecimal())
    #print(s.isspace())
    #print(s.istitle())
    if s.islower() or s.isupper() or s.isalpha() or s.isalnum() or s.isdecimal() or s.isspace() or s.istitle():
        print("No")
    else:
        print("Yes")
