# sourivong thepsimoung 
import sys 

class functions: 
    def __init__(self):
        super().__init__()
        self.title = title
        self.genre = genre
        self.rtime = rtime 
        self.rate = rate
        self.studio = studio
        self.year = year
        
    def description(self):
        print("Please choose one of the following options: ")
        print("1 -- Find all films produced by a certain studio")
        print("2 -- Find the Max film of a specific genre")
        print("3 -- FInd all films made in a given year range with a specific rating")
        print("4 -- Search for a film by a title")
        print("5 -- Find average runtime of films with a certain rating")
        print("6 -- Sort all lists by year and write the results to a new file") 
        print("7 -- Quit") 

    def openFile(self):
        good = False
        while good == False:
            fname = input("Enter file name: ")
            try:
                fn = open(fname, 'r')
                good = True
            except IOError:
                print("Invalid filename, try again")  
        return fn
              
    def getData(self, title, genre, rtime, rate, studio, year):
        fname = functions.openFile(self)
        for line in fname: 
            line = line.strip()
            t, g, rt, r, s, y = line.split(',')
            title.append(t)
            genre.append(g)
            rtime.append(rt)
            rate.append(r)
            studio.append(s)
            year.append(y)            
        fname.close()
        
        return title, genre, rtime, rate, studio, year
    
    def op_1(self, title, genre, rtime, rate, studio, year):
        found = False 

        while found == False:
            search = input("Enter studio: ")
            print("The films that meet your criteria are: ")  
            print("%-50s %-20s %-20s %-20s %-20s %-20s" %(title[0], genre[0], rtime[0], rate[0], studio[0], year[0]))
            
            if search in studio: 
                found = True
                for i in range(len(studio)):
                    if search == studio[i]:
                        t = title[i]
                        g = genre[i]
                        rt = rtime[i]
                        r = rate[i]
                        s = studio[i]
                        y = year[i]

                        print("%-50s %-20s %-20s %-20s %-20s %-20s" %(t, g, rt, r, s, y))
                        
            elif found == False:
                print("Invalid Choice - Try Again")
                functions.op_1(self, title, genre, rtime, rate, studio, year)
                
    def op_2(self, title, genre, rtime, rate, studio, year):
        Max = 0
        newT = []
        newG = []
        newRT = []
        newR = []
        newS = []
        newY = []
        search = input("Enter genre: ")
        print("Max Film with genre: ", search)
        if search in genre: 
            found = True
            for i in range(len(rtime)):
                if search == genre[i]:
                        newT.append(title[i])
                        newG.append(genre[i])
                        newRT.append(rtime[i])
                        newR.append(rate[i])
                        newS.append(studio[i])
                        newY.append(year[i])
                                             
        for i in range(len(newRT)):
            if int(newRT[Max]) <= int(newRT[i]):
                Max = i
        print("%-50s %-20s %-20s %-20s %-20s %-25s" %(title[0], genre[0], rtime[0], rate[0], studio[0], year[0]))
        print("%-50s %-20s %-20s %-20s %-20s %-25s" %(newT[Max], newG[Max], newRT[Max], newR[Max], newS[Max], newY[Max]))

    def op_3(self, title, genre, rtime, rate, studio, year):
        newT = []
        newG = []
        newRT = []
        newR = []
        newS = []
        newY = []
        good = False
        end = False
        print("Enter year range to search (oldest year first)")
        Min = int(input("Enter Year Min : "))
        Max = int(input("Enter Year Max: "))
        
        while good == False:
            if Min > Max: 
                print("Second year should be after year - try again")
                functions.op_3(functions, title, genre, rtime, rate, studio, year)
            else:
                good = True
                
        while good == True: 
            G = str(input("enter rating: "))
            print("The films that meet your criteria are: ")  
            
            if G in rate: 
                found = True
                for i in range(len(rtime)):
                    if  G == rate[i]:
                            newT.append(title[i])
                            newG.append(genre[i])
                            newRT.append(rtime[i])
                            newR.append(rate[i])
                            newS.append(studio[i])
                            newY.append(year[i])
                         
            for i in range(len(newY)):
                if int(newY[i]) >= Min and int(newY[i]) <= Max:
                    print("%-50s %-20s %-20s %-20s %-20s %-25s" %(newT[i], newG[i], newRT[i], newR[i], newS[i], newY[i]))
                end = True
            
            if end == True: 
                return 
                                          
def main():
    title = []
    genre = []
    rtime = []
    rate = []
    studio = []
    year = []
    functions.getData(functions, title, genre, rtime, rate, studio, year)
    functions.description(functions)  
    op = 0
    
    while op != 7: 
        op = int(input("Choice ==> "))
        if op == 1:
            functions.op_1(functions, title, genre, rtime, rate, studio, year)
        elif op == 2: 
            functions.op_2(functions, title, genre, rtime, rate, studio, year)
        elif op == 3: 
            functions.op_3(functions, title, genre, rtime, rate, studio, year)
        elif op == 4: 
            print("doesn't work")
            sys.exit() 
        elif op == 5: 
            print("doesn't work")
            sys.exit() 
        elif op == 6: 
            print("doesn't work")
            sys.exit()
        elif op == 7: 
            print("Goodbye.")
            sys.exit()              

if __name__ == "__main__":
    main()
