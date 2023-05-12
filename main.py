from tkinter import *
import commands

def window_clear():
    '''
    This Function clears the window of the previous widgets, making room for new ones.
    :return: only deletes and calls the second 'window' function.
    '''
    mainFrame.destroy()
    menu_tab()

def back_to_main():
    '''
    This function opens a new window, where the user can plug in new numbers if they wished
    :return: only deletes old widgets and starts up a new window.
    '''
    menuFrame.destroy()
    main()

def check_entries():
    '''
    this function converts the entered values into integers and sends them off into theri repected functions in commands.py
    this function will then take the returned values from the commands.py and plugs them into labels to display results.
    if any value/type error occures, then the user us promped by the exepction handling.
    :return: doesnt return anythign aside from the functions it calls in commands and the returns it recieves.
    '''
    global menuFrame
    menuFrame = Frame(shop)
    menuFrame.pack()
    error_label = None
    try:
        num_cookie = item_1_Entry.get()
        num_cookie = int(num_cookie)
        num_sandwich = item_2_Entry.get()
        num_sandwich = int(num_sandwich)
        num_water = item_3_Entry.get()
        num_water = int(num_water)
        num_soda = item_4_Entry.get()
        num_soda = int(num_soda)

        total_cookie = '$' + commands.cookie_function(num_cookie)
        print(total_cookie)
        total_sandwich = '$' + commands.sandwich_function(num_sandwich)
        print(total_sandwich)
        total_water = '$' + commands.water_function(num_water)
        print(total_water)
        total_soda = '$' + commands.soda_function(num_soda)
        print(total_soda)
        cart_total = '$' + commands.cart_total(num_cookie, num_sandwich, num_water, num_soda)
        print(cart_total)

        cart_label = Label(menuFrame, text='Cart Total: ', font=('Arial', 18))
        cart_label.grid(column=1, row=6)
        label_cart_total = Label(menuFrame, text=cart_total, font=('Arial', 18))
        label_cart_total.grid(column=3, row=6)

        item_1 = Label(menuFrame, text='Cookie Total: ', font=('Arial', 12))
        item_1.grid(column=1, row=1)
        total_item_1 = Label(menuFrame, text=total_cookie, font=('Arial', 12))
        total_item_1.grid(column=3, row=1)

        item_2 = Label(menuFrame, text='Sandwich Total: ', font=('Arial', 12))
        item_2.grid(column=1, row=2)
        total_item_2 = Label(menuFrame, text=total_sandwich, font=('Arial', 12))
        total_item_2.grid(column=3, row=2)

        item_3 = Label(menuFrame, text='Water Total: ', font=('Arial', 12))
        item_3.grid(column=1, row=3)
        total_item_3 = Label(menuFrame, text= total_water, font=('Arial', 12))
        total_item_3.grid(column=3, row=3)

        item_4 = Label(menuFrame, text='Soda Total: ', font=('Arial', 12))
        item_4.grid(column=1, row=4)
        total_item_4 = Label(menuFrame, text= total_soda, font=('Arial', 12))
        total_item_4.grid(column=3, row=4)

    except ValueError:
        print('Please Make Sure That All Item Entries Are Filled And Only Contain A Numerical Value!')
        error_label = Label(menuFrame, text='Please Fill All Entries With Numerical Values', font=('Arial', 12)).grid(column=2, row=7)

    except TypeError:
        print('Please Be Sure There Are No Decimals In Your Entries, Only Integers Are Accepted!')
        error_label = Label(menuFrame, text='Only Integers Are Accepted!',font=('Arial', 12)).grid(column=2, row=7)


def menu_tab():
    '''
    this function displays the menu prices and the entry boxes the user must fill out in order for the code to execute properly.
    this function also allows the user to calculate their cart value or they can be taken back to the home screen/page if so desired
    :return: this code recieves the entered values and sends it off to check_entries().
    '''
    global menuFrame
    menuFrame = Frame(shop)
    menuFrame.pack()

    menu_label = Label(menuFrame, text='Menu', font=('Bold', 18)).grid(column=1, row=0)
    item_1_label = Label(menuFrame, text='Cookie: $1.50', font=('Arial', 12)).grid(column=1, row=1)
    item_2_label = Label(menuFrame, text='Sandwich: $4.00', font=('Arial', 12)).grid(column=1, row=2)
    item_3_label = Label(menuFrame, text='Water: $1.00', font=('Arial', 12)).grid(column=1, row=3)
    item_4_label = Label(menuFrame, text='Soda: $1.75', font=('Arial', 12)).grid(column=1, row=4)

    global item_1_Entry, item_2_Entry, item_3_Entry, item_4_Entry
    item_1_Entry = Entry(menuFrame,font=('Arial', 12), width= 5)
    item_2_Entry = Entry(menuFrame, font=('Arial', 12), width= 5)
    item_3_Entry = Entry(menuFrame, font=('Arial', 12), width= 5)
    item_4_Entry = Entry(menuFrame, font=('Arial', 12), width= 5)
    item_1_Entry.grid(column=3, row=1)
    item_2_Entry.grid(column=3, row=2)
    item_3_Entry.grid(column=3, row=3)
    item_4_Entry.grid(column=3, row=4)

    checkout_button = Button(menuFrame, text= 'Checkout', font=('Arial', 12), command=check_entries).grid(column=1, row=5)
    back_to_home = Button(menuFrame, text= 'Back To Home', font=('Arial', 12), command=back_to_main).grid(column=3, row=5)

def main():
    '''
    this function is the main function that sets up the Tk() for the entire program/serves as the main menu page
    :return: user clicks either exit, which quits the program, or they can click browse menu to continue
    '''
    global shop
    shop = Tk()
    shop.geometry('350x350')
    shop.resizable(False, False)
    shop.title("Restraunt Menu")

    global mainFrame
    mainFrame = Frame(shop)
    mainFrame.pack()

    main_page_label = Label(mainFrame, text='Welcome To Our Market', font=('Bold', 18)).pack()
    mainToMenu_button = Button(mainFrame, text='  Browse Menu  ', font=('Arial', 12), command= window_clear).pack()
    main_exit_button = Button(mainFrame, text='  Exit App  ', font=('Arial', 12), command=shop.destroy).pack()

    shop.mainloop()

if __name__ == '__main__':
    main()