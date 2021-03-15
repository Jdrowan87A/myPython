import PH
import pay
import tkinter as tk
from functools import partial

##output function. Calls pay module to run calculations and displays them.
def all_output(data,frame,window,inp):
	frame.destroy()
	new_frame =tk.Frame(master = window, width= 55)
	new_frame.pack()
	if inp != 3:
		lbl_out = tk.Label(master = new_frame, width = 50,text = pay.calculate_taxes(data,inp))
		lbl_out.grid(row=0, column =0)
	elif inp == 3:
		lbl_out = tk.Label(master = new_frame, width =50, text = pay.calculate_required(data))
		lbl_out.grid(row=0,column=0)

	btn_main = tk.Button(master = new_frame, width = 15, text = "Back", command = lambda: loader_main(window,new_frame))
	window.bind('<Return>', lambda event=None: btn_main.invoke())
	btn_main.grid(row=1,column=0, pady=(15,15))

## button handler. Pulls in name of of the button and generates correct frame to gather new information.
def handle_button(name,old_frame,window):
	if name == "Exit":
		window.destroy()
	old_frame.destroy()
	if name == "Hourly":
		frm_info = tk.Frame(master = window, width= 50)
		frm_info.pack()

		lbl_hourly = tk.Label(master = frm_info, text="Hourly Rate:")
		lbl_hourly.grid(row = 0, column = 0)
		ent_hourly = tk.Entry(master = frm_info)
		ent_hourly.grid(row = 0, column = 1)
		lbl_return = tk.Label(master = frm_info)
		lbl_return.grid(row=2,column=1)

		ent_hourly.focus()

		btn_go = tk.Button(master = frm_info, text = "Go", command = lambda: all_output({"hourly":ent_hourly.get()},frm_info,window,1))
		window.bind('<Return>', lambda event=None: btn_go.invoke())
		btn_go.grid(row = 1, column = 0)

	if name == "Salary":
		frm_info = tk.Frame(master = window, width=50)
		frm_info.pack()

		lbl_sal = tk.Label(master = frm_info, text="Annual Salary:")
		lbl_sal.grid(row = 0, column = 0)
		ent_sal = tk.Entry(master = frm_info)
		ent_sal.grid(row = 0, column = 1)
		ent_sal.focus()
		lbl_return = tk.Label(master = frm_info)
		lbl_return.grid(row=2,column=1)



		btn_go = tk.Button(master = frm_info, text = "Go", command = lambda: all_output({"salary":ent_sal.get()},frm_info,window,2))
		window.bind('<Return>', lambda event=None: btn_go.invoke())
		btn_go.grid(row = 1, column = 0)

	if name == "Income Required":
		frm_info = tk.Frame(master = window, width=50)
		frm_info.pack()

		lbl_sal = tk.Label(master = frm_info, text = "Annual Salary Target:")
		lbl_sal.grid(row=0, column=0)
		ent_sal = tk.Entry(master = frm_info)
		ent_sal.grid(row = 0, column = 1)
		ent_sal.focus()

		btn_go = tk.Button(master =frm_info, text = "Go", command = lambda: all_output({"salary":ent_sal.get()},frm_info,window,3))
		window.bind('<Return>', lambda event=None: btn_go.invoke())
		btn_go.grid(row = 1, column = 0)

	if name == "Hourly Tips":
		frm_info = tk.Frame(master = window, width=50)
		frm_info.pack()

		lbl_hourly = tk.Label(master= frm_info, text = "Hourly wage:")
		lbl_hours = tk.Label(master= frm_info, text = "Average hours worked per day:")
		lbl_tips = tk.Label(master= frm_info, text = "Average tips per day:")
		lbl_days = tk.Label(master= frm_info, text = "Days per week:")

		ent_hourly = tk.Entry(master= frm_info)
		ent_hours = tk.Entry(master= frm_info)
		ent_tips = tk.Entry(master= frm_info)
		ent_days = tk.Entry(master= frm_info)

		lbl_hourly.grid(row=0 ,column=0)
		lbl_hours.grid(row=1 ,column=0)
		lbl_tips.grid(row=2 ,column=0)
		lbl_days.grid(row=3 ,column=0)
		ent_hourly.grid(row=0 ,column=1)
		ent_hours.grid(row=1 ,column=1)
		ent_tips.grid(row=2 ,column=1)
		ent_days.grid(row=3 ,column=1)
		ent_hourly.focus()

		btn_go = tk.Button(master =frm_info, text = "Go", command = lambda: all_output({"hourly":ent_hourly.get(),"hours":ent_hours.get(),"tips":ent_tips.get(),"days":ent_days.get()},frm_info,window,4))
		window.bind('<Return>', lambda event=None: btn_go.invoke())
		btn_go.grid(row = 4, column = 0)

	if name == "Hourly Overtime":
		frm_info = tk.Frame(master = window, width=50)
		frm_info.pack()

		lbl_hourly = tk.Label(master= frm_info, text = "Hourly wage:")
		lbl_hours = tk.Label(master= frm_info, text = "Averge OT per week:")
		lbl_rate = tk.Label(master= frm_info, text = "Rate of OT (1.5 is time and a half):")

		ent_hourly = tk.Entry(master= frm_info)
		ent_hours = tk.Entry(master= frm_info)
		ent_rate = tk.Entry(master= frm_info, text = "1.5")

		lbl_hourly.grid(row=0 ,column=0)
		lbl_hours.grid(row=1 ,column=0)
		lbl_rate.grid(row=2 ,column=0)
		ent_hourly.grid(row=0 ,column=1)
		ent_hours.grid(row=1 ,column=1)
		ent_rate.grid(row=2 ,column=1)

		ent_hourly.focus()

		btn_go = tk.Button(master =frm_info, text = "Go", command = lambda: all_output({"hourly":ent_hourly.get(),"overhours":ent_hours.get(),"rate":ent_rate.get()},frm_info,window,5))
		window.bind('<Return>', lambda event=None: btn_go.invoke())
		btn_go.grid(row = 3, column = 0)

##main window function, main menu
def loader_main(window,frame):
	frame.destroy()
	frm_one = tk.Frame(master= window, width = 150, bg="black")
	frm_one.pack()

	button_names = ["Hourly", "Salary", "Income Required", "Hourly Tips", "Hourly Overtime","Exit"]
	button_list=[]
	for name in button_names:
		button_list.append(tk.Button(master = frm_one, width = 15, text = name,relief = tk.GROOVE, borderwidth=2, command =lambda name=name: handle_button(name,frm_one,window)))
	for button in button_list:
		button.pack()
	button_list[0].focus()
###ENTRY POINT###	

window = tk.Tk()
window.geometry("550x250")
fr = tk.Frame()
loader_main(window,fr)


window.mainloop()