def is753(num):
    # 7,5,3がそれぞれ1回以上入っているかチェック
    if num.count('7') > 0 and num.count('5') > 0 and num.count('3') > 0:
        return True
    else:
        return False
