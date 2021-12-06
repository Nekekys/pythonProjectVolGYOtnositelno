# import keras
import numpy as np
import openpyxl
import matplotlib.pyplot as plt


table = openpyxl.open("Age_August_breast.xlsx", read_only=True)
sheet = table.active



inputValueDeepPointSubAxillary = []
inputValueDeepPointSubT = []

inputValueOutsidePointSubAxillary = []
inputValueOutsidePointSubT = []



year = []
j = 0
lastValue = ""

valueDeepPoint = 0
valueOutsidePoint = 0
valueDeepAxillary = 0
valueDeepT = 0
valueOutsideAxillary = 0
valueOutsideT = 0

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
            if i == 3:
                if (str(cell.value) == "здоровые МЖ здоровых") or (str(cell.value) == "норма-2"):
                    health = True
            if health:
                if i == 6:
                    valueDeepPoint = float(cell.value)
                if i == 14:
                    valueDeepAxillary = float(cell.value)
                if i == 16:
                    valueOutsidePoint = float(cell.value)
                if i == 24:
                    valueOutsideAxillary = float(cell.value)
                if (i > 5) and (i < 14):
                     sumDT += float(cell.value)
                if (i > 15) and (i < 24):
                    sumOT += float(cell.value)
                if i == 36:
                    valueDeepT = sumDT / 8
                    valueOutsideT = sumOT / 8
                    if str(cell.value) != "None":
                        year.append(int(cell.value))
                        check = True

            i += 1

    if check:
        inputValueDeepPointSubAxillary.append(round(valueDeepAxillary - valueDeepPoint, 2))
        inputValueDeepPointSubT.append(round(valueDeepT - valueDeepPoint, 2))

        inputValueOutsidePointSubAxillary.append(round(valueOutsideAxillary - valueOutsidePoint, 2))
        inputValueOutsidePointSubT.append(round(valueOutsideT - valueOutsidePoint, 2))

    j += 1


def sumFun(arr):
    sum = 0.0
    for el in arr:
        sum += el
    return sum / len(arr)




for i in range(len(year)):
    for j in range(len(year)):
        if year[i] > year[j]:
            t = year[i]
            year[i] = year[j]
            year[j] = t
            t1 = inputValueDeepPointSubAxillary[i]
            inputValueDeepPointSubAxillary[i] = inputValueDeepPointSubAxillary[j]
            inputValueDeepPointSubAxillary[j] = t1

            t2 = inputValueDeepPointSubT[i]
            inputValueDeepPointSubT[i] = inputValueDeepPointSubT[j]
            inputValueDeepPointSubT[j] = t2

            t3 = inputValueOutsidePointSubAxillary[i]
            inputValueOutsidePointSubAxillary[i] = inputValueOutsidePointSubAxillary[j]
            inputValueOutsidePointSubAxillary[j] = t3

            t4 = inputValueOutsidePointSubT[i]
            inputValueOutsidePointSubT[i] = inputValueOutsidePointSubT[j]
            inputValueOutsidePointSubT[j] = t4




def drowGraph(arr, title):
    x = year
    x_knots = year
    y_knots = arr

    poly_deg = 3
    coefs = np.polyfit(x_knots, y_knots, poly_deg)
    y_poly = np.polyval(coefs, x)

    plt.title(title)
    plt.plot(x_knots, y_knots, "o", label="data points")
    plt.plot(x, y_poly, label="polynomial fit")
    plt.legend()
    plt.show()




drowGraph(inputValueDeepPointSubAxillary, "Deep Axillary - Point1")
drowGraph(inputValueDeepPointSubT, "Deep T - Point1")
drowGraph(inputValueOutsidePointSubAxillary, "Outside Axillary - Point1")
drowGraph(inputValueOutsidePointSubT, "Outside T - Point1")


