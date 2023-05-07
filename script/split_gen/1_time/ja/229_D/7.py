def main():
    s = input()
    k = int(input())
    #print(s)
    #print(k)
    s = s.replace(".","X")
    #print(s)
    s = s.replace("X","X.")
    #print(s)
    s_list = s.split(".")
    #print(s_list)
    s_list = [i for i in s_list if i != ""]
    #print(s_list)
    if len(s_list) == 1:
        print(len(s_list[0]))
    else:
        if k >= len(s_list)-1:
            print(len(s))
        else:
            s_list.sort(key=lambda x:len(x))
            #print(s_list)
            l = len(s_list[0])
            for i in range(k):
                l += len(s_list[i+1])
            print(l)
