def main():
    S = input()
    o_count = S.count('o')
    x_count = S.count('x')
    question_count = S.count('?')
    if o_count > 4 or x_count == 10:
        print(0)
        return
    if o_count == 4:
        print(24)
        return
    if o_count == 3:
        print(36)
        return
    if o_count == 2:
        print(14 + 12 * question_count)
        return
    if o_count == 1:
        print(1 + 4 * question_count + 6 * question_count * (question_count - 1) / 2)
        return
    if o_count == 0:
        print(question_count * (question_count - 1) * (question_count - 2) * (question_count - 3) / 24)
        return

if __name__ == '__main__':
    main()