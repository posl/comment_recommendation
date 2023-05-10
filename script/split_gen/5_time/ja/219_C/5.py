def main():
    x = input()
    n = int(input())
    names = [input() for _ in range(n)]
    #print(x)
    #print(n)
    #print(names)
    #print(names[0])
    #print(names[1])
    #print(names[2])
    #print(names[3])
    #print(names[4])
    alpha = [0]*26
    for i in range(26):
        alpha[i] = x[i:i+1]
    #print(alpha)
    alpha_dict = dict()
    for i in range(26):
        alpha_dict[alpha[i]] = chr(97+i)
    #print(alpha_dict)
    names2 = []
    for name in names:
        name2 = ''
        for i in range(len(name)):
            name2 += alpha_dict[name[i:i+1]]
        names2.append(name2)
    #print(names2)
    names3 = []
    for i in range(len(names)):
        names3.append([names2[i],names[i]])
    #print(names3)
    names3.sort()
    #print(names3)
    for name in names3:
        print(name[1])
