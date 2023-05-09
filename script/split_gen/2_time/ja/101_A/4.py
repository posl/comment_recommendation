def main():
    s = input()
    cnt = 0
    for i in s:
        if i == '+':
            cnt += 1
        else:
            cnt -= 1
    print(cnt)
