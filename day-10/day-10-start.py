#Function with output

def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs." #terminate function early
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}" #output
    #if there are other lines of code after "return", it won't be executed as "return" is the output

print(format_name(input("What is your first name? "), input("What is your last name? ")))