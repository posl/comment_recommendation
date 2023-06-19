def main():
    s = [str(i) for i in input()]
    if s[0] == s[1] == s[2]:
        print('Won')
    else:
        print('Lost')
