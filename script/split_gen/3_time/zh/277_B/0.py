def main():
    #print("hello")
    #print("please input the number of strings:")
    #n = int(input())
    #print("please input the strings:")
    #s = []
    #for i in range(n):
    #    s.append(input())
    #print(s)
    #print("please input the strings:")
    s = ["H3","DA","D3","SK"]
    n = len(s)
    #print(n)
    if n != len(set(s)):
        print("No")
        return
    for i in range(n):
        if s[i][0] not in ['H','D','C','S']:
            print("No")
            return
        if s[i][1] not in ['A','2','3','4','5','6','7','8','9','T','J','Q','K']:
            print("No")
            return
    print("Yes")
    return
