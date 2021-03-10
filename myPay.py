import PH
import tkinter as tk

window = tk.Tk()
greeting = tk.Label(text= "Hello",
	fg = "white",
	bg = "black",
	width = 10,
	height = 10)

button1 = tk.Button(
	text= "Click",
	width = 3,
	height = 2,
	bg = "gray",
	fg = "white")
greeting.pack()
window.mainloop()



theInput = 0
while theInput != 6:
	print("Select: \n\
1 - Hourly\n\
2 - Salary\n\
3 - Total Annual Take Home Required\n\
4 - Hourly Add Overtime\n\
5 - Hourly Add Tips\n\
6 - Exit\n\
: : : ", end="")
	theInput = int(input())
	if theInput == 1 or theInput ==2:
		PH.calculate_taxes(theInput)
	elif theInput == 3:
		PH.calculate_required()
	elif theInput == 4:
		PH.calculate_taxes(theInput)
	elif theInput == 5:
		PH.calculate_taxes(theInput)
	elif theInput == 6:
		print("Goodbye!\n")
		break



	

		
	
	