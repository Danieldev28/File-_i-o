# file = open("a_new.txt","r+")
# file.write("something in here")
# #tells positon of cursor where is it now?
# print(file.tell())
# #you can seek anywhere in the document other then zero!
# file.seek(0)
# # you have to print the fil tell!
# print(file.tell())
# content = file.read()
# print(content)

cad_denom =[100,50,20,10,5,2,1,0.50,0.25,0.10,0.05,0.01]

p_amount = eval(input("You need change for what ammount? "))

def get_change(p_amount, cad_denom):
    if p_amount == int or type(p_amount) == float:
        final_change = []
        p_amount = round(float(p_amount),2)
        for denom in cad_denom:
            while denom <= p_amount:
                final_change.append(denom)
                p_amount = round(p_amount,2) - round(denom,2)
        print(final_change)
    else:
        print("its not and approppriate amount")

get_change(p_amount, cad_denom)    

    
