# Name: sourivong Thepsimoung 
# Date: May 12th 2020
# csc 110 Programming Project

import sys 

# class function for all options 
class functions: 

    # constructor function
    def __init__(self):
        super().__init__()
        self.title = title
        self.genre = genre
        self.rtime = rtime 
        self.rate = rate
        self.studio = studio
        self.year = year
        
    # describes the options
    def description(self):
        print("Please choose one of the following options: ")
        print("1 -- Find all films produced by a certain studio")
        print("2 -- Find the Max film of a specific genre")
        print("3 -- Find all films made in a given year range with a specific rating")
        print("4 -- Search for a film by a title")
        print("5 -- Find average runtime of films with a certain rating")
        print("6 -- Sort all lists by year and write the results to a new file") 
        print("7 -- Prints the Studio with the most films(extra)") 
        print("8 -- Quit") 

    # opens the given file
    def openFile(self):
        good = False

        # checks if file exists
        while good == False:
            fname = input("Enter file name: ")
            try:
                fn = open(fname, 'r')
                good = True
            except IOError:
                print("Invalid filename, try again")  
        return fn

    # reads a file and throw values into separate lists         
    def getData(self, title, genre, rtime, rate, studio, year):
        fname = functions.openFile(self)
        
        # reads line by line
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
    
    # Find all films produced by a certain studio
    def op_1(self, title, genre, rtime, rate, studio, year):
        found = False 

        while found == False:
            search = input("Enter studio: ")
            print("The films that meet your criteria are: ")  
            print("%-50s %-20s %-20s %-20s %-20s %-20s" %(title[0], genre[0], rtime[0], rate[0], studio[0], year[0]))
            
            # prints the films from studio
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
                        
            # check if studio exist
            elif found == False:
                print("Invalid Choice - Try Again")
                functions.op_1(self, title, genre, rtime, rate, studio, year)
                
    # Find the Max film of a specific genre
    def op_2(self, title, genre, rtime, rate, studio, year):
        
        # creates a new list containing selected genre
        newT = []
        newG = []
        newRT = []
        newR = []
        newS = []
        newY = []

        search = input("Enter genre: ")
        print("Max Film with genre: ", search)

        # adds selected film to new lists
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
                                             
        # runs through run time list to find max 
        Max = 0
        for i in range(len(newRT)):
            if int(newRT[Max]) <= int(newRT[i]):
                Max = i
        print("%-50s %-20s %-20s %-20s %-20s %-25s" %(title[0], genre[0], rtime[0], rate[0], studio[0], year[0]))
        print("%-50s %-20s %-20s %-20s %-20s %-25s" %(newT[Max], newG[Max], newRT[Max], newR[Max], newS[Max], newY[Max]))

    # Find all films made in a given year range with a specific rating
    def op_3(self, title, genre, rtime, rate, studio, year):
        
        # create new list to add specific rating only
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

        # checks Min is not greater than Max
        while good == False:
            if Min > Max: 
                print("Second year should be after year - try again")
                functions.op_3(functions, title, genre, rtime, rate, studio, year)
            else:
                good = True

        while good == True: 
            G = str(input("enter rating: "))
            print("The films that meet your criteria are: ")  
            
            # adds selected films to new list
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
                         
            # prints film from Min to Max only 
            for i in range(len(newY)):
                if int(newY[i]) >= Min and int(newY[i]) <= Max:
                    print("%-50s %-20s %-20s %-20s %-20s %-25s" %(newT[i], newG[i], newRT[i], newR[i], newS[i], newY[i]))
                end = True
            
            # ends the loop
            if end == True: 
                return 
    
    # Search for a film by a title
    def op_4(self, title, genre, rtime, rate, studio, year):
        End = False
        Found = False
        search = str(input("Enter title: "))

        # searches through list 
        for i in range(len(title)):
            if search == title[i]:
                print("The films that meet your criteria are: ")  
                print("%-50s %-20s %-20s %-20s %-20s %-20s" %(title[0], genre[0], rtime[0], rate[0], studio[0], year[0]))
                print("%-50s %-20s %-20s %-20s %-20s %-20s" %(title[i], genre[i], rtime[i], rate[i], studio[i], year[i]))
                Found = True
            else: 
                End = True
    
        if Found == True: 
            return 
        
        # if search doesn't exist
        elif Found == False: 
            print("invalid choice - try again")
            functions.op_4(self, title, genre, rtime, rate, studio, year)

    # Find average runtime of films with a certain rating
    def op_5(self, title, genre, rtime, rate, studio, year):
        newR = []
        value = 0
        good = False 
        search = str(input("enter rating: "))

        if search in rate: 
            good = True
        else:
            print("Invalid Choice - Try Again.")
            functions.op_5(self, title, genre, rtime, rate, studio, year)
        
        if good == True: 
            for i in range(len(rtime)):
                if  search == rate[i]:
                    newR.append(rtime[i])

            # calculates the avg
            for i in range(len(newR)):
                value += int(newR[i])
        
            Total = round(value/len(newR),2)
        
        print("The average runtime for films with a", search, "rating is", Total)
    
    # Sort all lists by year and write the results to a new file
    def op_6(self, title, genre, rtime, rate, studio, year):
        
        # sorting algorithm to sort each list
        for i in range(1, len(year)):
            Min = i 
            for j in range(i, len(year)):
                if year[j] < year[Min]:
                    Min = j
            title[i], title[Min] = title[Min], title[i]
            genre[i], genre[Min] = genre[Min], genre[i]
            rtime[i], rtime[Min] = rtime[Min], rtime[i]
            rate[i], rate[Min] = rate[Min], rate[i]
            studio[i], studio[Min] = studio[Min], studio[i]
            year[i], year[Min] = year[Min], year[i]
            
        name = input("Enter the name of output file: ")
        ofile = open(name, 'w')

        # loop to write out each lines into the output file
        for x in range(len(year)):
            ofile.write(title[x] + "," + genre[x] + "," + rtime[x] +","+ rate[x] + ","+ studio[x]+ "," + year[x] + '\n')
        ofile.close()
        print("The File is now in your library.")
        return

    # Prints the Studio with the most films (extra credit)
    def op_7(self, title, genre, rtime, rate, studio, year):
        Total = 0
        maxStudio = studio[0]

        # loop that finds most frequent of an element
        # note: count is a built-in function. Not suitable 
        # for class assignments. 
        for i in studio:
            currMax = studio.count(i)

            # sets current Max to new Max 
            if currMax > Total:
                Total = currMax
                maxStudio = i

        print("The studio that made the most film is:",maxStudio,"with a total of:", Total)

def main():

    # creates a list for all values of a file 
    title = []
    genre = [] 
    rtime = []
    rate = []
    studio = []
    year = []
    functions.getData(functions, title, genre, rtime, rate, studio, year)
    functions.description(functions)  
    op = 0
    
    # input loop that ranges from 1-8 
    # where 8 is the exit input command. 
    while op != 8: 
        op = int(input("Choice ==> "))
        if op == 1:
            functions.op_1(functions, title, genre, rtime, rate, studio, year)
        elif op == 2: 
            functions.op_2(functions, title, genre, rtime, rate, studio, year)
        elif op == 3: 
            functions.op_3(functions, title, genre, rtime, rate, studio, year)
        elif op == 4: 
            functions.op_4(functions, title, genre, rtime, rate, studio, year) 
        elif op == 5: 
            functions.op_5(functions, title, genre, rtime, rate, studio, year) 
        elif op == 6: 
            functions.op_6(functions, title, genre, rtime, rate, studio, year) 
        elif op == 7:
            functions.op_7(functions, title, genre, rtime, rate, studio, year) 
        elif op == 8: 
            print("Goodbye.")
            sys.exit()              

if __name__ == "__main__":
    main()
