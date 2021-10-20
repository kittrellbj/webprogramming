################################################
# TipCalc.py                                   #
# Collects input about the user's bill         #
# and returns the appropriate tip.             #
# @auth: Brian Kittrell                        #
# @date: 10/20/2021                            #
################################################

# Declarations/input
billTotal = 0.0
tipPercent = [0.15, 0.20]
userBill = input("Enter total bill amount: ")

# Main
try:
    float(userBill)
except ValueError as error:
    print("Must enter a decimal number like XX.XX without the dollar sign. Error: ", error, sep="")
else:
    for item in tipPercent:
        billTip = float(userBill) * item
        print("$", round(billTip, 2), " is the ", (item * 100), "% tip on $", round(float(userBill), 2), ". Total with tip: $", round((billTip + float(userBill)), 2), sep="")