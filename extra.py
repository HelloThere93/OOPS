string="*"

for i in range(0,10,1):
    print(string*i)


string="*"

for i in range(10,0,-1):
    print(string*i)


for i in range(0,10,1):
    a = []
    for j in range(0,i,1):
       
        a.append(j)
        print(a)
