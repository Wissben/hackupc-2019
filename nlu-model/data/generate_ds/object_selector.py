f = open('data.txt','r')
out = open('data.single','w+')
for line in f.readlines():
    if len(line.split())==1:
        out.write(line)

out.close()
f.close()
