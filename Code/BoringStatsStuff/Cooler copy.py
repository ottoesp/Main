d = input('Enter Numbers: ').split(', ')
data = []
for i in d:
    data.append(float(i))
data = sorted(data)
print(data)
length = len(data)


print('minimum', data[0])
print('maximum', data[-1])

if (length % 2) == 0:
    median_1 = (data[length//2])
    median_2 = (data[length//2 - 1])
    median = ((median_1 + median_2)/2)

else:
    median = (data[length//2])
print('median', median)


fqr = data[:int(median)]
length = len(fqr)

if (length % 2) == 0:
    median_1 = (fqr[length//2])
    median_2 = (fqr[length//2]-1)
    median = ((median_1 + median_2)/2)

else:
    median = (data[length//2])
print('first quartile', median)

tqr = data[int(median):]
length = len(tqr)

if (length % 2) == 0:
    median_1 = (tqr[length//2])
    median_2 = (tqr[length//2 + 1])
    median = ((median_1 + median_2)/2)
    
else:
    median = (data[length//2])
print('third quartile', median)
