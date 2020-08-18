data = input().split()
length = len(data)
for i in data:
    int(i)
    print(i)
print('minimum', data[0])
print('maximum', data[-1])
if (length % 2) != 0:
    medno = int(length/2)
else:
    medno = lenght/2
print(medno)
print(data)


