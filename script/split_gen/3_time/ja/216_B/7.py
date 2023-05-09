def main():
    n = int(input())
    st = []
    for _ in range(n):
        s, t = input().split()
        st.append(s + t)
    if len(set(st)) == n:
        print('No')
    else:
        print('Yes')
