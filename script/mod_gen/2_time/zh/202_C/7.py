def main():
    s = input()
    #s = "0601889"
    s = s[::-1]
    #print(s)
    s = s.replace("0","a")
    s = s.replace("1","b")
    s = s.replace("6","c")
    s = s.replace("8","d")
    s = s.replace("9","e")
    s = s.replace("a","0")
    s = s.replace("b","1")
    s = s.replace("c","9")
    s = s.replace("d","8")
    s = s.replace("e","6")
    print(s)
main()
