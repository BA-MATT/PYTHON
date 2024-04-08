 
first_name = input("Pease enter your first name :")
last_name = input("Pease enter your last name:")



def Title_name(fn,ln):
    fn1 = fn.title()   
    ln1 = ln.title() 
    return f"{fn1}  {ln1}"

full_nme= Title_name(first_name,last_name)
print(full_nme)