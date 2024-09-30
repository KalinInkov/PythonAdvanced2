def sorting_cheeses(**kwargs):
    result =""

    sorted_cheeses = sorted(kwargs.items(), key=lambda kvp: (-len([kvp]),kvp[0]))

    for cheese_name, quantity in sorted_cheeses:
        result+=f"{cheese_name}\n"
        sorted_quantity_list = sorted(quantity,reverse=True)
        result+="\n".join([str(x) for x in sorted_quantity_list])+"\n"



    return result

print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)
