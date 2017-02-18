import numpy as np


def main():

    try:
        date, rate, arb = np.loadtxt('/Users/kachunfung/python/datamining/TutSheet.csv', delimiter=',', unpack=True, dtype='str')

        x = 0
        for eachDate in date[:-1]:
            saveLine = eachDate + ',' + rate[x]+ ','+ arb[x] + ',' + str(int(arb[x])+ 3) + '\n'
            saveFile = open('newCSV.csv', 'a')
            saveFile.write(saveLine)
            saveFile.close()
            x += 1

        saveLine = date[-1] + ',' + rate[-1]+ ','+ arb[-1] + ',' + str(int(arb[-1])+ 1000)
        saveFile = open('newCSV.csv', 'a')
        saveFile.write(saveLine)
        saveFile.close()


    except Exception, e:
        print str(e)

main()
