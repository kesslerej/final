# Given money in one currency it tranfers it into a different specified currency


def change_currency(amount, currency, new_currency):
    currencies = ["Dollar", "Euro", "Pound", "Bitcoin", "all"]
    if new_currency not in currencies:
        sorry = "Im sorry, that currency doesn't seem to be in our system"
        return sorry
    if currency not in currencies:
        sorry = "Im sorry, '%s' doesn't seem to be in our system." % currency
        return sorry

        
    for n in range(0, len(currencies)):
        if currency == "Dollar":
            if new_currency == "Euro":
                Euro_conversion = .85
                return amount * Euro_conversion, new_currency + "s"

            elif new_currency == "Pound":
                Pound_conversion = .75
                return amount * Pound_conversion, new_currency + "s"

            elif new_currency == "Bitcoin": 
                Bitcoin_conversion = 0.000058
                return amount * Bitcoin_conversion, new_currency + "s"

            elif new_currency == "all":
                Euro_conversion = .85
                Pound_conversion = .75
                Bitcoin_conversion = 0.000058

                return amount * Euro_conversion, 'Euros', \
                        amount * Pound_conversion, 'Pounds', \
                        amount * Bitcoin_conversion, 'Bitcoins'

        elif currency == "Euro":
            if new_currency == "Dollar":
                Dollar_conversion = 1.18
                return amount * Dollar_conversion, new_currency + "s"

            elif new_currency == "Pound":
                Pound_conversion = 0.88
                return amount * Pound_conversion, new_currency + "s"

            elif new_currency == "Bitcoin": 
                Bitcoin_conversion = 0.000068
                return amount * Bitcoin_conversion, new_currency + "s"
 
            elif new_currency == "all":
                Dollar_conversion = 1.18
                Pound_conversion = 0.88
                Bitcoin_conversion = 0.000068

                return (amount * Dollar_conversion, 'Dollars', \
                        amount * Pound_conversion, 'Pounds', \
                        amount * Bitcoin_conversion, 'Bitcoins')

        elif currency == "Pound":
            if new_currency == "Dollar":
                Dollar_conversion = 1.34
                return amount * Dollar_conversion, new_currency + "s"

            elif new_currency == "Euro":
                Euro_conversion = 1.14
                return amount * Euro_conversion, new_currency + "s"

            elif new_currency == "Bitcoin": 
                bitocin_conversion = 0.000078
                return amount * Bitcoin_conversion, new_currency + "s"

            elif new_currency == "all":
                Dollar_conversion = 1.34
                Euro_conversion = 1.14
                Bitcoin_conversion = 0.000078

                return (amount * Dollar_conversion, 'Dollars', \
                        amount * Euro_conversion, 'Euros', \
                        amount * Bitcoin_conversion, 'Bitocins')

        elif currency == "Bitcoin":
            if new_currency == "Dollar":
                Dollar_conversion = 17241.24
                return amount * Dollar_conversion, new_currency + "s"

            elif new_currency == "Euro":
                Euro_conversion = 14656.77
                return amount * Euro_conversion, new_currency + "s"

            elif new_currency == "Pound": 
                Pound_conversion = 12899.89
                return amount * Pound_conversion, new_currency + "s"

            elif new_currency == "all":
                Dollar_conversion = 17241.24
                Euro_conversion = 14656.77
                Pound_conversion = 12899.89

                return ((amount * Dollar_conversion), " Dollars", \
                        (amount * Euro_conversion), " Euros", \
                        (amount * Pound_conversion), " Pounds")



print "How much money would you like to convert?"
amount = float(raw_input())
print ("\n")
print "What currency do you use? Here are your options:"
print "Dollar, Euro, Pound, Bitcoin"
currency = raw_input()
print ("\n")
print "What other currencies do you want to change it to? Here are your options:"
print "Dollar, Euro, Pound, Bitcoin, all"
new_currency = raw_input()
print ("\n")
print change_currency(amount, currency, new_currency)