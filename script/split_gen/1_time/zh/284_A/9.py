def main():
    n = int(input())
    s_list = []
    for i in range(n):
        s_list.append(input())
    for i in range(n-1,-1,-1):
        print(s_list[i])
