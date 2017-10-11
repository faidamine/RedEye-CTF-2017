n = int(raw_input())
name = list()
ch = list()
sss = list()
rrr = list()
zzz = list()

aaa =list()

lll=list()

for i in range(0,n):
    a = raw_input()
    r = a.split(" ")
    name.append(r)
    ch.append(r[1])
    rrr.append(r[2])
    aaa.append(r[0])

for f in range(0,n):
    for j in range(0, n-f):
        c = sorted(aaa)

        if name[j][0] == c[f]:
            sss.append(name[j])

            name.remove(name[j])
            break

for f in range(0,n):
    for j in range(0, n-f):
        c = sorted(rrr,reverse=True)

        if sss[j][2] == c[f]:
            zzz.append(sss[j])

            sss.remove(sss[j])
            break

for f in range(0,n):
    for j in range(0, n-f):
        c = sorted(ch,reverse=True)

        if zzz[j][1] == c[f]:
            lll.append(zzz[j])

            zzz.remove(zzz[j])
            break
			
print "\n"
for name in lll:
    print name[0]