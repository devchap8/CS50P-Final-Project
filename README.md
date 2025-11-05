# Starter Project Collection
#### Description: A collection of three common starter projects I made from scratch
## Projects:
### TicTacToe:
#### Takes a column and a row as user input and places an X or an O every turn
#### Displays the grid every turn in the command line
#### Checks if the vertical, horizontal, or diagonal lines match and grants a win to the X or O player
#### The grid is stored as a list of three nested lists, and the values of the nested lists are checked to see if a player has won or if a move is valid
### ToDo List:
#### Uses a ToDoList class containing the item title, the priority of the item, the type of the item, and the details of the item
#### Users can manually add items in the command line with the add() function
##### Takes one input of title, priority, type, and details separated by commas
##### Checks if the title is unique (to make changing and removing possible) and if the priority is a 1-10 int, and that all items are present
#### Users can manually remove items with the remove() function
#### Users can change one aspect of an item with the change() function
##### If the user changes the title, program checks to make sure title is unique
##### If the user changes the priority, program checks to make sure the priority is a 1-10 int
#### Users can see their list with the list() function
##### Items are sorted from highest priority (1) to lowest priority (10)
#### Users can see a list of commands with the help() function
#### Users can export their list to a .csv with the export() function
#### Users can import their todo list from a .csv file with the import_file() function
##### Can let the user override the whole list or add the items from the file to the existing list
##### If user chooses to add, items from the file with the same title as an already existing item will not be added
### Currency Exchange:
#### Using the currency_converter library, users can convert a certain amount from one currency to another
##### Takes an integer, the currency to be converted from, and the currency to be converted to separated by a comma and a space
#### Optionally, users can also input a year to do the conversion
#### User can see a list of currencies by typing "currencies" or see a list of commands by typing "help"
### Main Program:
#### The project.py program connects the three programs and takes user input to start them
#### Calling project.py thanks in the command line displays an easter egg!
