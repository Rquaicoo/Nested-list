a = []
b=[]
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        a.append(name)
        a.append(score)
        b.append(a)
        a = []
c = []
for  x in range(len(b)):
    c.append(b[x][1])
c = min(c)
d = []
for x in range(len(b)):
    if b[x][1] > c:
        d.append(b[x][1])
e = min(d)
f = []
for x in range(len(b)):
    if b[x][1] == e:
        f.append(b[x][0])
f.sort()
for x in range(len(f)):
    print(f[x])
    
