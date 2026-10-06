print("Welcome to Library Management System!")
print("Please select an option.")
print("Library Management System")
#i sucessfully connected pycharm and git hub
#hi how are you 
from member import member
from library import  Library


def main():
    library = Library()

    # Load books from the data file
    library.load_books("data/books.txt")

    # Create members
    member1 = member(1, "Rahul")
    member2 = member(2, "Priya")

    library.add_member(member1)
    library.add_member(member2)

    print("BOOKS")
    print("-----------------------------")
    library.show_books()

    print("\nIssuing book...")
    library.issue_book(101, 1)

    print("\nBOOKS AFTER ISSUE")
    print("-----------------------------")
    library.show_books()

    print("\nReturning book...")
    library.return_book(101, 1)

    print("\nBOOKS AFTER RETURN")
    print("-----------------------------")
    library.show_books()


if __name__ == "__main__":
    main()
