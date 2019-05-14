aray = []

for i in range(100):
    aray.append(i)

def addall(s,n):
    if len(s) != 0:
        addall(s[1:], n + s[0])
    else:
        print(n)

addall(aray,0)
