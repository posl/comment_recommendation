def judge(s):
    if s <= "2019/04/30":
        print("Heisei")
    else:
        print("TBD")
s = input()
judge(s)

if __name__ == '__main__':
    judge()