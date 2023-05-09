def main():
    #s = [input() for _ in range(10)]
    #s = [input() for _ in range(10)]
    s = []
    for _ in range(10):
        s.append(input())
    #print(s)
    for i in range(10):
        s[i] = s[i].replace(".", "0")
        s[i] = s[i].replace("#", "1")
    #print(s)
    s = [int(i) for i in s]
    #print(s)
    for i in range(10):
        if s[i] == 1:
            s[i] = 0
        else:
            s[i] = 1
    #print(s)
    for i in range(10):
        s[i] = str(s[i])
    #print(s)
    for i in range(10):
        s[i] = s[i].replace("0", ".")
        s[i] = s[i].replace("1", "#")
    #print(s)
    for i in range(10):
        print(s[i])
