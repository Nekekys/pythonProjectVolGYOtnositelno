# import keras
import numpy as np
import openpyxl
import matplotlib.pyplot as plt


table = openpyxl.open("dataset_illarion_to_clf.xlsx", read_only=True)
sheet = table.active



inputValueDeepPointSubAxillary = []
inputValueDeepPointSubT1 = []
inputValueDeepPointSubT2 = []

inputValueOutsidePointSubAxillary = []
inputValueOutsidePointSubT1 = []
inputValueOutsidePointSubT2 = []


year = []
yearIZ = 0
yearValue = 0

j = 0
lastValue = ""

valueDeepPoint = 0
valueOutsidePoint = 0
valueDeepAxillary = 0
valueDeepT1 = 0
valueDeepT2 = 0
valueOutsideAxillary = 0
valueOutsideT1 = 0
valueOutsideT2 = 0

k = 0
for row in sheet.iter_rows():

    sumDT = 0
    sumOT = 0
    i = 0
    check = False
    checkTest = False
    health = False


    for cell in row:
        if j != 0:
            if i == 189:
                if str(cell.value) == "0":
                    health = True

            if i == 46:
                valueDeepPoint = float(cell.value)
            if i == 54:
                valueDeepAxillary = float(cell.value)
            if i == 56:
                valueOutsidePoint = float(cell.value)
            if i == 64:
                valueOutsideAxillary = float(cell.value)
            if i == 65:
                valueDeepT1 = float(cell.value)
            if i == 66:
                valueDeepT2 = float(cell.value)
            if i == 67:
                valueOutsideT1 = float(cell.value)
            if i == 68:
                valueOutsideT2 = float(cell.value)
            if i == 11:
                yearIZ = int(cell.value)
            if i == 15:
                yearValue = yearIZ - int(cell.value)

            i += 1

    if health and valueDeepPoint - valueDeepAxillary > -4.5 and yearValue > 15:
        year.append(yearValue)
        inputValueDeepPointSubAxillary.append(round(valueDeepPoint - valueDeepAxillary, 2))
        inputValueDeepPointSubT1.append(round(valueDeepPoint - valueDeepT1, 2))
        inputValueDeepPointSubT2.append(round(valueDeepPoint - valueDeepT2, 2))

        inputValueOutsidePointSubAxillary.append(round(valueOutsidePoint - valueOutsideAxillary, 2))
        inputValueOutsidePointSubT1.append(round(valueOutsidePoint - valueOutsideT1, 2))
        inputValueOutsidePointSubT2.append(round(valueOutsidePoint - valueOutsideT2, 2))


    j += 1



def sumFun(arr):
    sum = 0.0
    for el in arr:
        sum += el
    return sum / len(arr)


unique_year = list(set(year))
sorted(unique_year)

# for i in range(len(year)):
#     for j in range(len(year)):
#         if year[i] > year[j]:
#             t = year[i]
#             year[i] = year[j]
#             year[j] = t
#             t1 = inputValueDeepPointSubAxillary[i]
#             inputValueDeepPointSubAxillary[i] = inputValueDeepPointSubAxillary[j]
#             inputValueDeepPointSubAxillary[j] = t1
#
#             t2 = inputValueDeepPointSubT1[i]
#             inputValueDeepPointSubT1[i] = inputValueDeepPointSubT1[j]
#             inputValueDeepPointSubT1[j] = t2
#
#             t9 = inputValueDeepPointSubT2[i]
#             inputValueDeepPointSubT2[i] = inputValueDeepPointSubT2[j]
#             inputValueDeepPointSubT2[j] = t9
#
#             t3 = inputValueOutsidePointSubAxillary[i]
#             inputValueOutsidePointSubAxillary[i] = inputValueOutsidePointSubAxillary[j]
#             inputValueOutsidePointSubAxillary[j] = t3
#
#             t4 = inputValueOutsidePointSubT1[i]
#             inputValueOutsidePointSubT1[i] = inputValueOutsidePointSubT1[j]
#             inputValueOutsidePointSubT1[j] = t4
#
#             t5 = inputValueOutsidePointSubT2[i]
#             inputValueOutsidePointSubT2[i] = inputValueOutsidePointSubT2[j]
#             inputValueOutsidePointSubT2[j] = t5

inputValueDeepPointSubAxillaryM = []
inputValueDeepPointSubT1M = []
inputValueDeepPointSubT2M = []

inputValueOutsidePointSubAxillaryM = []
inputValueOutsidePointSubT1M = []
inputValueOutsidePointSubT2M = []
for annum in unique_year:
    elemDeepA = []
    elemDeepT1 = []
    elemDeepT2 = []
    elemOutsideA = []
    elemOutsideT1 = []
    elemOutsideT2 = []
    t = 0
    for elem in year:
        if (annum == elem):
            elemDeepA.append(inputValueDeepPointSubAxillary[t])
            elemDeepT1.append(inputValueDeepPointSubT1[t])
            elemDeepT2.append(inputValueDeepPointSubT2[t])
            elemOutsideA.append(inputValueOutsidePointSubAxillary[t])
            elemOutsideT1.append(inputValueOutsidePointSubT1[t])
            elemOutsideT2.append(inputValueOutsidePointSubT2[t])
        t += 1

    inputValueDeepPointSubAxillaryM.append(round(np.median(elemDeepA), 2))
    inputValueDeepPointSubT1M.append(round(np.median(elemDeepT1), 2))
    inputValueDeepPointSubT2M.append(round(np.median(elemDeepT2), 2))
    inputValueOutsidePointSubAxillaryM.append(round(np.median(elemOutsideA), 2))
    inputValueOutsidePointSubT1M.append(round(np.median(elemOutsideT1), 2))
    inputValueOutsidePointSubT2M.append(round(np.median(elemOutsideT2), 2))


def drowGraph(arr, title):
    x = unique_year
    x_knots = unique_year
    y_knots = arr

    poly_deg = 3
    coefs = np.polyfit(x_knots, y_knots, poly_deg)
    y_poly = np.polyval(coefs, x)

    plt.title(title)
    plt.plot(x_knots, y_knots, "o", label="data points")
    plt.plot(x, y_poly, label="polynomial fit")
    plt.legend()
    plt.show()




drowGraph(inputValueDeepPointSubAxillaryM, "Deep Point1 - Axillary")
drowGraph(inputValueDeepPointSubT1M, "Deep T1 - ")
drowGraph(inputValueDeepPointSubT2M, "Deep T2 - Point1")
drowGraph(inputValueOutsidePointSubAxillaryM, "Outside Axillary - Point1")
drowGraph(inputValueOutsidePointSubT1M, "Outside T1 - Point1")
drowGraph(inputValueOutsidePointSubT2M, "Outside T2 - Point1")


