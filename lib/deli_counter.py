katz_deli = ["Ada", "Grace", "Kent"]

def take_a_number(katz_deli, name):
    print(f"Welcome, {name}. You are number {len(katz_deli)+1} in line.")
    return katz_deli.append(name)



def line(katz_deli):
    if len(katz_deli) == 0:
        print("The line is currently empty.")
    else:
        print_list = []
        for index, name in enumerate(katz_deli):
            print_list.append((f"{index+1}. {name}"))
            queue = " ".join(print_list) 
        print(f"The line is currently: {queue}") 

# line(katz_deli)

def now_serving(katz_deli):
        if len(katz_deli) == 0:
            print("There is nobody waiting to be served!")
        else:
            print(f"Currently serving {katz_deli[0]}.")
            katz_deli.pop(0)    

now_serving(katz_deli)
