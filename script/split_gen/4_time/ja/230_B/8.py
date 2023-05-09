def main():
    s = input()
    
    if len(s) >= 1 and len(s) <= 10:
        if s.count('o') == 0:
            print('No')
        else:
            print('Yes')
