def safe_or_unsafe(s,w):
    if w>=s:
        return "unsafe"
    else:
        return "safe"

if __name__ == '__main__':
    safe_or_unsafe()