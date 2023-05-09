def is_satisfied(s):
    """S が問題文中の条件を満たすか判定する関数
    Args:
        s (str): 文字列
    Returns:
        str: S が条件を満たすなら Yes、満たさないなら No
    """
    if not s[0].isupper():  # S の先頭の文字が英大文字でない場合
        return "No"
    if not s[-1].isupper():  # S の末尾の文字が英大文字でない場合
        return "No"
    if s[1:-1].isdecimal():  # S の先頭と末尾の文字を除いた文字列が整数である場合
        if 100000 <= int(s[1:-1]) <= 999999:  # S の先頭と末尾の文字を除いた文字列が 100000 以上 999999 以下の整数である場合
            return "Yes"
    return "No"

if __name__ == '__main__':
    is_satisfied()