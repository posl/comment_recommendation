def main():
    n = int(input())
    dict = {}
    for i in range(n):
        s,t = input().split()
        if s in dict:
            dict[s] += 1
        else:
            dict[s] = 1
        if t in dict:
            dict[t] += 1
        else:
            dict[t] = 1
    for key in dict:
        if dict[key] > 1:
            print('No')
            return
    print('Yes')
    return
