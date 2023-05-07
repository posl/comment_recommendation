def main():
    n = int(input())
    st = []
    for i in range(n):
        st.append(input().split())
    for i in range(n):
        for j in range(n):
            if i != j:
                if st[i][0] == st[j][0] and st[i][1] == st[j][1]:
                    print('No')
                    exit()
    print('Yes')

if __name__ == '__main__':
    main()