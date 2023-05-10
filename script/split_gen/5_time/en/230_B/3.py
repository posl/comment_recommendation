def main():
    s = input()
    t = 'o' + s + 'o'
    if t.find('oxxo') == -1:
        print('No')
    else:
        print('Yes')
