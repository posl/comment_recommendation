def main():
    N = int(input())
    c = input()
    r = c.count('R')
    w = c.count('W')
    if r == 0 or w == 0:
        print(0)
    else:
        print(min(r,c.rfind('R')+1,w,c.find('W')+1))
