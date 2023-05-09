def main():
    s1=input()
    s2=input()
    s3=input()
    t=input()
    d={'1':s1,'2':s2,'3':s3}
    s=''
    for i in t:
        s=s+d[i]
    print(s)

if __name__ == '__main__':
    main()