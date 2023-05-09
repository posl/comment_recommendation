def main():
    S = input()
    if S.rfind('a') == -1:
        print(-1)
    else:
        print(S.rfind('a')+1)
