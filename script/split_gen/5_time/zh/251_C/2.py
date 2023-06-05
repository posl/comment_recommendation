def main():
    n = int(input())
    dict = {}
    for i in range(n):
        s, t = input().split()
        if s not in dict:
            dict[s] = [i+1, int(t)]
        else:
            if int(t) > dict[s][1]:
                dict[s] = [i+1, int(t)]
    max = 0
    for k, v in dict.items():
        if v[1] > max:
            max = v[1]
            ans = v[0]
    print(ans)
