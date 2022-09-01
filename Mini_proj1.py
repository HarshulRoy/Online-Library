class Library:
    def __init__(self,name,List):
        self.name=name
        self.List=List
        self.dict={}
    def display(self):
        print(f"displaying the books present in {self.name}")
        for books in self.List:
            print(books)
    def lendbook(self,user,book):
        if book in self.dict.keys():
            print(f"book is already lended to {self.dict[book]}")
        else :
            print("book lend database has been updated, you can use book now")
            self.dict.update({book:user})
    def addbook(self,book):
        if book not in self.List:
            self.List.append(book)
            print(f"book has been added to {self.name}")
    def returnbook(self,book):
        if book in self.dict.keys():
            self.dict.pop(book)
            print("book has been added successfully")
List=["harry potter","python","C++","man vs wild","jungle book"]
harshul=Library("mylib",List)
if __name__ == '__main__':
    while(True):
        print("welcome to library\n","press 1 to display books\n","press 2 to lend a book\n","press 3 to add a book\n","press 4 to return a book\n","Press 5 to pass")
        choice1=int(input("Enter the number"))
        if choice1==1:
            harshul.display()
        elif choice1==2:
            a=input("Enter the user name")
            b=input("Enter the book name")
            harshul.lendbook(a,b)
        elif choice1==3:
            a=input("Enter the book you want to add")
            harshul.addbook(a)
        elif choice1==4:
            a=input("Enter the book you want to return")
            harshul.returnbook(a)
        elif choice1==5:
            pass
        else:
            print("invalid input please try again")
            continue
        choice2=input("press q to quit and c to continue")
        while (True):

           if choice2=="q":
              break
           elif choice2=="c":
              break
           else :
               print("invalid input ")
               choice2=input("Enter again")
        if choice2=="q":
            print("Exiting the library")
            break
        else:
            continue












