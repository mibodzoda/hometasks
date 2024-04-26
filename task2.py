def common(a, b):
    c = [ i for i in a if i in b]
    return c
a = input().split()
b = input().split()
print(common(a, b))