from ast import keyword


def main():

    try:
        #initialize books list
        booksList = []
        infile = open("theBooksList.txt", "r")
        line = infile.readline()
        while line:
            booksList.append(line.rstrip("\n").split(","))
            line = infile.readline()
        infile.close()

    except FileNotFoundError:
        print("the <bookslist.txt> file is not found")
        print("Starting a new bookslist")
        booksList = []


    choice = 0
    while choice != 4:
        print("---Book Manager---")
        print("1. Add a book")
        print("2. Search a book")
        print("3. Display books")
        print("4. Quit")
        choice = int(input())

        if choice == 1:
            print("Adding a book")
            nBook = input("Enter the name of the book>>>")
            nAuthor = input("Enter the name of the author>>>")
            nPages = input("Enter the number of pages>>>")
            booksList.append([nBook, nAuthor,nPages])

        elif choice == 2:
            print("Searching for a book?")
            keyword = input("Please enter your book here")
            for book in booksList:
                if keyword in book:
                    print(book)

        elif choice == 3:
            print("Displaying all the books")
            for book in booksList:
                print(book)
        
        elif choice == 4:
            print("Quitting program")
    print("Program Terminated!")

    #Saving to external TXT file
    outfile = open("theBooksList.txt", "w")
    for book in booksList:
        outfile.write(",".join(book) + "\n")
    outfile.close()




            




if __name__=="__main__":
    main()
