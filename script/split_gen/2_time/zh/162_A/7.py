def judge(n):
    if n%10 == 7:
        return True
    elif n//10%10 == 7:
        return True
    elif n//100 == 7:
        return True
    else:
        return False
n = int(input())
