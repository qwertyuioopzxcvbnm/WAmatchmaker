from comp import matches
import pandas
from sendemail import sendResults


filename = "file.csv"
data = pandas.read_csv(filename)
data = pandas.DataFrame(data)


personcomp = 0

def compare(sub, sys):
    n = 0
    for i in range(10, 28):
        
        if data.iloc[sub, i] == data.iloc[sys, i]:
            
            n = n+1
            
        else:
            pass
    return n/18*100



def percent(person):
    

    comp = matches(person)
    templist = []
    for obj in comp:
        a = [obj, round(compare(person, obj), 2)]
        templist.append(a)

    sorted_templist = sorted(templist, key=lambda x: x[1], reverse=True)
    sorted_templist = sorted_templist[:5]
    sorted_templist.insert(0, data.iloc[person, 1])
    

    return sorted_templist

def customize(change, number):
    ind = percent(change)
    ind.pop(-1)
    num = ind[1][1]+1/18
    lis = [number, num]
    ind.insert(1, lis)
    return ind


def printResults(person):
    list = percent(person)
    formattedList = []
    row_index = data[data.iloc[:, 1] == list[0]].index[0]
    formattedList.append(data.iloc[row_index, 2])
    for i in range(1, len(list)):
        personnumber = list[i][0]
        templist = []
        templist.append(data.iloc[personnumber,2])
        templist.append(list[i][1])
        formattedList.append(templist)
    print(formattedList)



printResults(92)
