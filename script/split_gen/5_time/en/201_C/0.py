def main():
    s = input()
    print(s.count('o')*100 + s.count('?')*100 - s.count('x')*100 + s.count('o')*10 + s.count('?')*10 - s.count('x')*10 + s.count('o') + s.count('?') - s.count('x'))
