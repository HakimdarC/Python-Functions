
res = []
for i in range(101):
    if(i%2==0):
        res.append(i)
print(res)

print([i for i in range(101) if i%2==0])
