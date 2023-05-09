def poor(a,b,c):
    if a==b and b!=c:
        return "Yes"
    elif a==c and c!=b:
        return "Yes"
    elif b==c and c!=a:
        return "Yes"
    else:
        return "No"
a,b,c=map(int,input().split())
print(poor(a,b,c))

if __name__ == '__main__':
    poor()