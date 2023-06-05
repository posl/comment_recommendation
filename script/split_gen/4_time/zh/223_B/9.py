def main():
    s = input()
    s = s * 2
    s_min = s[0:len(s)//2]
    s_max = s[0:len(s)//2]
    for i in range(1,len(s)//2):
        s_min = min(s_min,s[i:i+len(s)//2])
        s_max = max(s_max,s[i:i+len(s)//2])
    print(s_min)
    print(s_max)
