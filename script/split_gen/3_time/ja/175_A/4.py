def main():
    S = input()
    cnt = 0
    max = 0
    for i in range(3):
        if S[i] == 'R':
            cnt += 1
            if cnt > max:
                max = cnt
        else:
            cnt = 0
    print(max)
