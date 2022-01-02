def new_line():     #new_line is a new defined function, and the function calls the argument to print a .
    print(".")

def three_lines():  #three_lines i a new defined function, and the function calls the function new_line three times to print .
    new_line()
    new_line()
    new_line()
    
def nine_lines():   #nine_lines is a new defined function, and the function calls the function three_lines three times that calles the function new_line
    three_lines()
    three_lines()
    three_lines()

nine_lines()

def clear_screen():  #clear_screen calls the nine_lines function twice which produces 18 lines, the three_lines twice which equals 24 lines total, new_line once making a total of 25 lines
    new_line()
    three_lines()
    three_lines()
    nine_lines()
    nine_lines()

print("Calling clearScreen()") #print function separates the 9 lines from the 25
clear_screen()
