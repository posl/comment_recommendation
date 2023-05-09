def main():
    S = input()
    S_list = list(S)
    for s in S_list:
        if S_list.count(s) == 1:
            print(s)
            exit()
    print(-1)
