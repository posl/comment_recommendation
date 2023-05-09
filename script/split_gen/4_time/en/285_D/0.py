def readinput():
    n=int(input())
    st=[]
    for _ in range(n):
        s,t=input().split()
        st.append((s,t))
    return n,st
