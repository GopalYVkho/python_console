class library():
    def __init__(self,list):
        self.booklist = list
        self.available_books_list  =list[:]
        self.book_lent={}


    def available_books(self):
        for book in self.available_books_list:
            print(book)

    def all_books(self):
        for book in self.booklist:
            print(book)

    def lent_book(self,name,book):
        if book not in self.booklist:
            print("Incorrect Book name,Please check Book list")
        if book in self.available_books_list:
            self.book_lent.update({book:name})
            self.available_books_list.remove(book)
            print("You Can take the book..")
        else:
            print("The book is already by "+self.book_lent[book])

    def return_book(self,book):
        del self.book_lent[book]
        self.available_books_list.append(book)




if __name__=="__main__":
    lib=library(["Ponniyin Selvan","Aram","Oru Puliyamarathin Kathai","Moga Mul","Yamam"])
    print("Welcome To Library,Enter an option ")
    while True:
        print("1. Display Available Books ")
        print("2. Display All Books")
        print("3. Borrow A Book")
        print("4. Return A Book")
        print("5. Quit")
        user_chooice = int(input())
        if user_choice == 1:
            lib.available_books()
        elif user_chooice == 2:
            lib.all_books()
        elif user_choice == 3:
            name=input("Enter Your Name")
            book=input("Enter Your Book")
            lib.lent_book(name,book)
        elif user_choice == 4:
            book=input("Enter Your Book")
            lib.return_book(book)
        elif user_choice == 5:
            break
        else:
            print("ENTER 1 To 5 NUMBERS ONLY")
