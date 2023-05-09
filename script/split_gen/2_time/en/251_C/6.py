def main():
    n = int(input())
    dict = {}
    for i in range(n):
        s, t = input().split()
        if s in dict:
            dict[s].append([i, int(t)])
        else:
            dict[s] = [[i, int(t)]]
    max = 0
    max_index = 0
    for key, value in dict.items():
        if len(value) == 1:
            if value[0][1] > max:
                max = value[0][1]
                max_index = value[0][0]
        else:
            value.sort(key=lambda x: x[1], reverse=True)
            if value[0][1] > max:
                max = value[0][1]
                max_index = value[0][0]
    print(max_index + 1)
