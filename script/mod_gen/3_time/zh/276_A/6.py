def lastIndex(s):
    #请在这里编写代码
    if s.rfind('a') == -1:
        print(-1)
    else:
        print(s.rfind('a')+1)

if __name__ == '__main__':
    lastIndex()