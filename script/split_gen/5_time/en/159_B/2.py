def main():
    s = input()
    if s == s[::-1]:
        if s[:int((len(s)-1)/2)] == s[:int((len(s)-1)/2):-1] and s[int((len(s)+3)/2)-1:] == s[int((len(s)+3)/2)-1::-1]:
            print("Yes")
        else:
            print("No")
    else:
        print("No")
