# Student Account System (Commandline Interface)
## Lunch money system task
You must design a system to store the amount of money a student has for lunch and to carry out the top up and purchase processes involved in a schools lunch system.
Your program must include the following:
*	The ability to load information for a student from a file containing 10 students and their current account balance using their code.
*	A text-based menu which allows a student to choose to either ‘top-up’ their account or ‘purchase’ a food item as explained below
____

* Top-up – asks the user to enter which coins/notes they are entering one at a time from the following choices: ***10p, 20p, 50p, £1, £2, £5, £10, £20.***  
  As each coin value is entered it should be added to the current account balance and return the new account balance.
  The final balance should be returned once the user has finished.
 * Purchase – the user is presented with 10 different food options and can choose from as many as they like from the menu.  
   After each food choice the price of the food should be removed from the students account.
   If the subtraction leads to a negative balance then a message saying `“Not enough funds for this transaction”` should appear and the student should have the chance to choose again or finish.  
   The final balance after all food transitions should be displayed at the end.

Data items to be used:

`DataList1`
Student code|	Student Firstname|	Student Surname|	Account balance|
| ------------- |:-------------:| :-----:| :----------:|
JH02|	Jeremy|	Harris|	£0.50|
SR02|	Sara|	Reyes|	£10.00|
KP01|	Kimberley|	Power|	£8.60|
DT12|	Donald|	Thompson|	£24.00|
CH01|	Carl|	Hampton-Bose|	£16.30|
DH16|	Dean|	Harris|	£1.40|
EE01|	Evie|	Evelyn|	£9.10|
AJ05|	Amiee|	Jarvis|	£5.60|
AJ06|	Andrew|	Jacobs|	£3.20|
YK03|	Youssef|	Khan|	£0.70|

`DataList2`

|Food item|	Cost
| --- |:---:|
Pizza slice|	£1.20|
Pasta pot|	£1.50|
Main meal	|£2.80|
Panini|	£1.50|
Sandwich|£1.70|
Premium Sandwich|	£2.10|
Sausage Roll|	£1.10|
Salad	|£1.60|
Dessert|	£1.00|
Jacket potato|	£1.00|

*This was a project set by my teacher*
