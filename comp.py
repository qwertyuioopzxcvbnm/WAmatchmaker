import pandas
from email.message import EmailMessage
import re


filename = "file.csv"


data = pandas.read_csv(filename)
data = pandas.DataFrame(data)




def clean_data(value):
    return re.sub(r'\w+\)', '', value).strip()


def matches(compPerson):
    matchlist = []
    for i in range(len(data)):
        gradePref = clean_data(data.iloc[compPerson,9])
        personGrade = clean_data(data.iloc[i,6])
        genderPref = clean_data(data.iloc[compPerson,8])
        personGender = clean_data(data.iloc[i,7])

        if personGender in genderPref and personGrade in gradePref:
            gradePref = clean_data(data.iloc[i,9])
            personGrade = clean_data(data.iloc[compPerson,6])
            genderPref = clean_data(data.iloc[i,8])
            personGender = clean_data(data.iloc[compPerson,7])
            if personGender in genderPref and personGrade in gradePref:
                matchlist.append(data.iloc[i, 2])
    
    return matchlist  
print(matches(279))
