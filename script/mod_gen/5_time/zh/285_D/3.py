def handle(s,t):
    if s==t:
        return False
    if len(s)!=len(t):
        return False
    if len(s)>8 or len(s)<1 or len(t)>8 or len(t)<1:
        return False
    return True
n=int(input())

if __name__ == '__main__':
    handle()