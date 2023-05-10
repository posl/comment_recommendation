def main():
    x = input()
    n = int(input())
    s = [input() for _ in range(n)]
    x_dic = {x[i]: chr(97 + i) for i in range(len(x))}
    s.sort(key=lambda x: ''.join([x_dic[x[i]] for i in range(len(x))]))
    print(*s, sep='\n')
