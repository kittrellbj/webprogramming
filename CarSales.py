################################################
# CarSales.py                                  #
# Collects input about the car involved in the #
# sale and returns the total cost.             #
# @auth: Brian Kittrell                        #
# @date: 10/20/2021                            #
################################################

# Declarations/input
defaultFees = [
    ["Dealer Prep Fee", 400],
    ["License", .03],
    ["Clear Coat Protection Program", 500],
    ["Tax", .07],
    ["Destination", 200],
    ["Gap Coverage", 150]
]
inputCost = input("- > Enter MSRP of vehicle: ")

# Main
try:
    vehicleCost = float(inputCost)
except ValueError as error:
    print("Cost must be entered as a number. Error: ", error, sep="")
else:
    print("\t- > Car Sales Invoice:")
    vehicleTotalCost = vehicleCost
    for title, value in defaultFees:
        if title == "Tax":
            print("\t\t", title, ": $", round((vehicleCost * value), 2), "*", sep="")
            vehicleTotalCost += vehicleCost * value
        elif title == "License":
            print("\t\t", title, ": $", round((vehicleCost * value), 2), "*", sep="")
            vehicleTotalCost += vehicleCost * value
        else:
            print("\t\t", title, ": $", value, sep="")
            vehicleTotalCost += value
    print("\t- > Total cost: $", vehicleTotalCost, sep="")
    print("\t\t* 7% tax and 3% license fee calculated only against MSRP. Taxes already\n\t\tincluded in all other fees.")