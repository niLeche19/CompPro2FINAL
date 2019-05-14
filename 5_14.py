aray = []

for i in range(2500):
    aray.append(i)

def addall(s,n):
    if len(s) != 0:
        addall(s[1:], n + s[0])
    else:
        print(n)

def SUM(n):
    a = 0
    for i in range(n):
        a += i
    print(a)

def FIBO(n):
    if n == 0:
        return(1)
    if n == 1:
        return(1)
    else:
        return (FIBO(n-1) + FIBO(n-2))

def fibo(l,n):
    lst = l
    if n+2 <= len(lst):
        for i in l:
            print(i)
    else:
        lst.append(lst[len(lst)-1] + lst[len(lst)-2])
        fibo(l, n-1)

# fibo([1,1], 30)
# print(FIBO(10))




if d <= 1:
        draw_point(x, y)                 # base case
    else:
        # recurse on upper left quadrant
        draw_sierpinsky(x, y, d/2)
        # recurse on upper right quadrant
        draw_sierpinsky(x + d/2, y, d/2)
        # recurse on lower right quadrant
        draw_sierpinsky(x + d/2, y + d/2, d/2)
        
