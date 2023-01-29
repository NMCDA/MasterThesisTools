# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import np as np
import numpy
import numpy as np
import pandas
from sklearn import linear_model
import matplotlib.pyplot as plt

def average_hosp(csv, country, year):
    f = open(csv, "r")
    average = 0
    Sum = 0
    row_count = 0
    for row in f:
        column = row.split(',')
        if column[0].split('-')[0] == year and column[1] == country and column[3] == "00+":
                n = float(column[5])
                Sum += n
                row_count += 1
    average = Sum / row_count
    f.close()
    print('The average for country ' + country + ' in year ' + year + ' is:' + str(average))


def average_inz(csv, country, year):
    f = open(csv, "r")
    average = 0
    Sum = 0
    row_count = 0
    for row in f:
        column = row.split(',')
        if column[0].split('-')[0] == year and column[1] == country and column[2] == "00+":
                n = float(column[7])
                Sum += n
                row_count += 1
    average = Sum / row_count
    f.close()
    print('The average for country ' + country + ' in year ' + year + ' is:' + str(average))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    df = pandas.read_csv("2021.csv")
    '''
    #Hospitalisierungen:
    average_hosp("hosp.csv", "Schleswig-Holstein", "2020")
    average_hosp("hosp.csv", "Schleswig-Holstein", "2021")
    average_hosp("hosp.csv", "Schleswig-Holstein", "2022")

    average_hosp("hosp.csv", "Hamburg", "2020")
    average_hosp("hosp.csv", "Hamburg", "2021")
    average_hosp("hosp.csv", "Hamburg", "2022")

    average_hosp("hosp.csv", "Niedersachsen", "2020")
    average_hosp("hosp.csv", "Niedersachsen", "2021")
    average_hosp("hosp.csv", "Niedersachsen", "2022")

    average_hosp("hosp.csv", "Bremen", "2020")
    average_hosp("hosp.csv", "Bremen", "2021")
    average_hosp("hosp.csv", "Bremen", "2022")

    average_hosp("hosp.csv", "Nordrhein-Westfalen", "2020")
    average_hosp("hosp.csv", "Nordrhein-Westfalen", "2021")
    average_hosp("hosp.csv", "Nordrhein-Westfalen", "2022")

    average_hosp("hosp.csv", "Hessen", "2020")
    average_hosp("hosp.csv", "Hessen", "2021")
    average_hosp("hosp.csv", "Hessen", "2022")

    average_hosp("hosp.csv", "Rheinland-Pfalz", "2020")
    average_hosp("hosp.csv", "Rheinland-Pfalz", "2021")
    average_hosp("hosp.csv", "Rheinland-Pfalz", "2022")

    average_hosp("hosp.csv", "Baden-Württemberg", "2020")
    average_hosp("hosp.csv", "Baden-Württemberg", "2021")
    average_hosp("hosp.csv", "Baden-Württemberg", "2022")

    average_hosp("hosp.csv", "Bayern", "2020")
    average_hosp("hosp.csv", "Bayern", "2021")
    average_hosp("hosp.csv", "Bayern", "2022")

    average_hosp("hosp.csv", "Saarland", "2020")
    average_hosp("hosp.csv", "Saarland", "2021")
    average_hosp("hosp.csv", "Saarland", "2022")

    average_hosp("hosp.csv", "Berlin", "2020")
    average_hosp("hosp.csv", "Berlin", "2021")
    average_hosp("hosp.csv", "Berlin", "2022")

    average_hosp("hosp.csv", "Brandenburg", "2020")
    average_hosp("hosp.csv", "Brandenburg", "2021")
    average_hosp("hosp.csv", "Brandenburg", "2022")

    average_hosp("hosp.csv", "Mecklenburg-Vorpommern", "2020")
    average_hosp("hosp.csv", "Mecklenburg-Vorpommern", "2021")
    average_hosp("hosp.csv", "Mecklenburg-Vorpommern", "2022")

    average_hosp("hosp.csv", "Sachsen", "2020")
    average_hosp("hosp.csv", "Sachsen", "2021")
    average_hosp("hosp.csv", "Sachsen", "2022")

    average_hosp("hosp.csv", "Sachsen-Anhalt", "2020")
    average_hosp("hosp.csv", "Sachsen-Anhalt", "2021")
    average_hosp("hosp.csv", "Sachsen-Anhalt", "2022")

    average_hosp("hosp.csv", "Thüringen", "2020")
    average_hosp("hosp.csv", "Thüringen", "2021")
    average_hosp("hosp.csv", "Thüringen", "2022")

    #Inzidenzen:
    average_inz("inzidenz.csv", "01", "2020")
    average_inz("inzidenz.csv", "01", "2021")
    average_inz("inzidenz.csv", "01", "2022")

    average_inz("inzidenz.csv", "02", "2020")
    average_inz("inzidenz.csv", "02", "2021")
    average_inz("inzidenz.csv", "02", "2022")

    average_inz("inzidenz.csv", "03", "2020")
    average_inz("inzidenz.csv", "03", "2021")
    average_inz("inzidenz.csv", "03", "2022")

    average_inz("inzidenz.csv", "04", "2020")
    average_inz("inzidenz.csv", "04", "2021")
    average_inz("inzidenz.csv", "04", "2022")

    average_inz("inzidenz.csv", "05", "2020")
    average_inz("inzidenz.csv", "05", "2021")
    average_inz("inzidenz.csv", "05", "2022")

    average_inz("inzidenz.csv", "06", "2020")
    average_inz("inzidenz.csv", "06", "2021")
    average_inz("inzidenz.csv", "06", "2022")

    average_inz("inzidenz.csv", "07", "2020")
    average_inz("inzidenz.csv", "07", "2021")
    average_inz("inzidenz.csv", "07", "2022")

    average_inz("inzidenz.csv", "08", "2020")
    average_inz("inzidenz.csv", "08", "2021")
    average_inz("inzidenz.csv", "08", "2022")

    average_inz("inzidenz.csv", "09", "2020")
    average_inz("inzidenz.csv", "09", "2021")
    average_inz("inzidenz.csv", "09", "2022")

    average_inz("inzidenz.csv", "10", "2020")
    average_inz("inzidenz.csv", "10", "2021")
    average_inz("inzidenz.csv", "10", "2022")

    average_inz("inzidenz.csv", "11", "2020")
    average_inz("inzidenz.csv", "11", "2021")
    average_inz("inzidenz.csv", "11", "2022")

    average_inz("inzidenz.csv", "12", "2020")
    average_inz("inzidenz.csv", "12", "2021")
    average_inz("inzidenz.csv", "12", "2022")

    average_inz("inzidenz.csv", "13", "2020")
    average_inz("inzidenz.csv", "13", "2021")
    average_inz("inzidenz.csv", "13", "2022")

    average_inz("inzidenz.csv", "14", "2020")
    average_inz("inzidenz.csv", "14", "2021")
    average_inz("inzidenz.csv", "14", "2022")

    average_inz("inzidenz.csv", "15", "2020")
    average_inz("inzidenz.csv", "15", "2021")
    average_inz("inzidenz.csv", "15", "2022")

    average_inz("inzidenz.csv", "16", "2020")
    average_inz("inzidenz.csv", "16", "2021")
    average_inz("inzidenz.csv", "16", "2022")
    '''
    X = df[['kurzarbeit', 'arbeitslosigkeit', 'digital']]
    y = df['inzidenz']

    regr = linear_model.LinearRegression()
    print("")
    regr.fit(X, y)

    predictedCO2 = regr.coef_
    print(predictedCO2)

    t0 = pandas.read_csv("2020.csv")
    t1 = pandas.read_csv("2021.csv")
    t2 = pandas.read_csv("2022.csv")

    hosp = np.concatenate((t0['hosp'].values,t1['hosp'].values,t2['hosp'].values), axis=0)
    inz = np.concatenate((t0['inzidenz'].values,t1['inzidenz'].values,t2['inzidenz'].values), axis=0)
    kz = np.concatenate((t0['kurzarbeit'].values,t1['kurzarbeit'].values,t2['kurzarbeit'].values), axis=0)
    al = np.concatenate((t0['arbeitslosigkeit'].values,t1['arbeitslosigkeit'].values,t2['arbeitslosigkeit'].values), axis=0)
    di = np.concatenate((t0['digital'].values,t1['digital'].values,t2['digital'].values), axis=0)


    print(inz)
    print(kz)
    print(al)
    print(di)


    #create basic scatterplot
    plt.plot(inz, kz, 'o')
    plt.xlabel("7-Tage-Inzidenz")
    plt.ylabel("Kurzarbeiterquote")
    #obtain m (slope) and b(intercept) of linear regression line
    m, b = np.polyfit(inz, kz, 1)

    #add linear regression line to scatterplot
    plt.plot(inz, m*inz+b)

    plt.show()