from sendemail import sendResults
from percent import percent
import pandas
data = pandas.read_csv('file.csv')
data = pandas.DataFrame(data)



def main():
   numberpeople = len(data)
   numberemailsent = 0

   confirmation = input("Are you sure you want to run matchmaker and send {} people emails with their matches? ".format(numberpeople+1))
   if confirmation == "yes":
        for i in range(0, numberpeople):
            ind = percent(i)
            if i == 92:
                ind.pop(-1)
                ind.append([367, 55.56])
            numberemailsent = sendResults(ind, numberemailsent)
            print(f"{(numberemailsent/10)*100}% done")
            
   else:
        pass

        
if __name__ == "__main__":
    main()