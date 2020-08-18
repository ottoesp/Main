d = input('Data: ').split(', ')

#5 figure summary (
data = []

for i in d:
    data.append(float(i))
data = sorted(data)
length = len(data)
median = 0

def Mediancode(x, y):
    r = data[x:y]
    length = len(r)
    if (length % 2) == 0:

        median_1 = (r[length//2])
        median_2 = (r[length//2-1])
        median = ((median_1 + median_2)/2)

    else:
        median = (data[length//2])
    
    return(median)

median = Mediancode(0, length)

intmedian = int(median)
minimum = data[0]

first_quartile = Mediancode(0, intmedian-1)

final = data.index(data[-1])+1

third_quartile = Mediancode(intmedian, final)

maximum = data[-1]
# )

# Outliers (

def Outliers(d):
    data = []

    for i in d:
        data.append(float(i))

    iqr = third_quartile - first_quartile

    outliers = []

    for i in data:
        if i < first_quartile - iqr*1.5:
            outliers.append(i)
        elif i > third_quartile + iqr*1.5:
            outliers.append(i)

    print('Outliers:', outliers)

    return outliers

#Outliers

print(Outliers(d))
print('Minimum:', minimum)
print('First quartile:', first_quartile)
print('Median:', median)
print('Third quartile:', third_quartile)
print('Maximum:', maximum)
