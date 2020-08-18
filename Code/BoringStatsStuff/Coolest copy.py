d = input('Enter Numbers: ').split(', ')
data = []

for i in d:
    data.append(float(i))
data = sorted(data)
length = len(data)
median = 0


# Works out median of given data set
def MedianCode(x, y, data):
    r = data[x:y]
    print('r',r)
    length = len(r)
    if (length % 2) == 0:

        median_1 = r[round(length / 2)]
        median_2 = r[round(length / 2 - 1)]
        median = ((median_1 + median_2) / 2)

    else:
        median = (data[round(length / 2-1)])

    return median


median2 = MedianCode(0, length, data)

intMedian = round(median2)

print('intMedian', intMedian)

minimum = data[0]
print('Minimum:', minimum)

print('Median:', median2)

firstQuartile = MedianCode(None, intMedian - 1, data)
print('First quartile:', firstQuartile)

thirdQuartile = MedianCode(intMedian, None, data)

print('Third quartile:', thirdQuartile)


maximum = data[-1]
print('Maximum:', maximum)


# -10, 1, 2, 3, 5, 7, 10
