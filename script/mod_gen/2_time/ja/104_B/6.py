def main():
    #入力
    s = input()
    #先頭の文字が'A'かどうか
    if s[0] != 'A':
        print('WA')
        return
    #3文字目と末尾から2文字目の間に'C'がちょうど1個含まれるかどうか
    if s[2:-1].count('C') != 1:
        print('WA')
        return
    #それ以外の文字はすべて小文字であるかどうか
    if s[1:].replace('C', '').islower() == False:
        print('WA')
        return
    print('AC')
    return

if __name__ == '__main__':
    main()