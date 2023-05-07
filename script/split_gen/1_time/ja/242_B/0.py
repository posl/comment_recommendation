def main():
    S = input()
    S_list = list(S)
    S_list.sort()
    ans = ''.join(S_list)
    print(ans)
