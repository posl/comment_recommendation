def main():
    s = input()
    # 辞書順で最小の文字列は、文字列をソートしたもの
    print(''.join(sorted(s)))

if __name__ == '__main__':
    main()