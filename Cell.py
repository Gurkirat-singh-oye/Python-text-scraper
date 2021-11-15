import csv
import semipermeable_membrane as semi
import the_system as ts

def cell():
    ofile = open('Output.csv','a')
    oile = csv.writer(ofile)
    oile.writerow(['URL_ID','URL','POSITIVE SCORE','NEGATIVE SCORE','POLARITY SCORE'
                ,'SUBJECTIVITY SCORE','AVG SENTENCE LENGTH','PERCENTAGE OF COMPLEX WORDS'
                ,'FOG INDEX','COMPLEX WORD COUNT','SYLLABLE PER WORD','AVG WORD LENGTH'
                ,'WORD COUNT','PERSONAL PRONOUNS'])
    ofile.close()
    file = open('Input - Copy.csv')
    csvfile = csv.reader(file, delimiter=',')

    ofile = open('Output.csv','a')
    oile = csv.writer(ofile)

    for a in csvfile:

        #semi.URL.append(a[1])

##    for a in semi.URL:
        print(f"working for URL_id {a[0]}...")
        ctx = semi.scoping(a[1])
        if ctx == None:
            pass
        else:
            results = []
            food = semi.membrane(ctx)
            ilikdiz = ts.cleanfood(food)
            results = (ts.PNPoS(ilikdiz) + ts.SlCwF(food) 
                + [len(ilikdiz.split())] + ts.perspros(food))
            
            
            oile.writerow([a[0]]+[a[1]]+results)

    ofile.close()
    file.close()

cell()
