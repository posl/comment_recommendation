def main():
    n = int(input())
    s = [input() for _ in range(n)]
    s_set = set(s)
    for s_ in s:
        if s_[0] == '!':
            s_ = s_[1:]
        else:
            s_ = '!' + s_
        if s_ in s_set:
            print(s_)
            return
    print('satisfiable')
    return
