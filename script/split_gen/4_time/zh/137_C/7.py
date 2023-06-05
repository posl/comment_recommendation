def count(s):
    dic={}
    for i in s:
        dic[i]=dic.get(i,0)+1
    return dic
