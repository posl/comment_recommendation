def main():
    n = int(input())
    st = []
    for i in range(n):
        s,t = input().split()
        st.append((s,int(t)))
    st.sort(key=lambda x: x[0])
    st.sort(key=lambda x: x[1], reverse=True)
    print(st[0][0])
