def judge_bust(a1, a2, a3):
    if a1 + a2 + a3 >= 22:
        return 'bust'
    else:
        return 'win'

if __name__ == '__main__':
    judge_bust()