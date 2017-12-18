# Given money in one currency it tranfers it into a different specified currency


def change_currency(amount, currency, new_currency):
    currencies = ["dollar", "euro", "pound", "bitcoin", "all"]
    if new_currency not in currencies:
        sorry = "Im sorry, that currency doesn't seem to be in our system"
        return sorry
    if currency not in currencies:
        sorry = "Im sorry, that currency doesn't seem to be in our system"
        return sorry
        
    for n in range(0, len(currencies)):
        if currency == "dollar":
            if new_currency == "euro":
                euro_conversion = .85
                return amount * euro_conversion

            elif new_currency == "pound":
                pound_conversion = .75
                return amount * pound_conversion

            elif new_currency == "bitcoin": 
                bitcoin_conversion = 0.000058
                return amount * bitcoin_conversion

            elif new_currency == "all":
                euro_conversion = .85
                pound_conversion = .75
                bitcoin_conversion = 0.000058

                return amount * euro_conversion, 'euros', \
                        amount * pound_conversion, 'Pounds', \
                        amount * bitcoin_conversion, 'bitcoins'

        elif currency == "euro":
            if new_currency == "dollar":
                dollar_conversion = 1.18
                return amount * dollar_conversion

            elif new_currency == "pound":
                pound_conversion = 0.88
                return amount * pound_conversion

            elif new_currency == "bitcoin": 
                bitcoin_conversion = 0.000068
                return amount * bitcoin_conversion
 
            elif new_currency == "all":
                dollar_conversion = 1.18
                pound_conversion = 0.88
                bitcoin_conversion = 0.000068

                return (amount * dollar_conversion, 'Dollars', \
                        amount * pound_conversion, 'Pounds', \
                        amount * bitcoin_conversion, 'bitcoins')

        elif currency == "pound":
            if new_currency == "dollar":
                dollar_conversion = 1.34
                return amount * dollar_conversion

            elif new_currency == "euro":
                euro_conversion = 1.14
                return amount * euro_conversion

            elif new_currency == "bitcoin": 
                bitocin_conversion = 0.000078
                return amount * bitcoin_conversion

            elif new_currency == "all":
                dollar_conversion = 1.34
                euro_conversion = 1.14
                bitcoin_conversion = 0.000078

                return (amount * dollar_conversion, 'Dollars', \
                        amount * euro_conversion, 'euros', \
                        amount * bitcoin_conversion, 'Bitocins')

        elif currency == "bitcoin":
            if new_currency == "dollar":
                dollar_conversion = 17241.24
                return amount * dollar_conversion

            elif new_currency == "euro":
                euro_conversion = 14656.77
                return amount * euro_conversion

            elif new_currency == "pound": 
                pound_conversion = 12899.89
                return amount * pound_conversion

            elif new_currency == "all":
                dollar_conversion = 17241.24
                euro_conversion = 14656.77
                pound_conversion = 12899.89

                return (amount * dollar_conversion, 'Dollars', \
                        amount * euro_conversion, 'euros', \
                        amount * pound_conversion, 'Pounds')



print "How much money would you like to convert?"
amount = float(raw_input())
print ("\n")
print "What currency do you use? Here are your options:"
print "dollar, euro, pound, bitcoin"
currency = raw_input()
print ("\n")
print "What other currencies do you want to change it to? Here are your options:"
print "dollar, euro, pound, bitcoin, all"
new_currency = raw_input()
print ("\n")
print new_currency, "-", change_currency(amount, currency, new_currency)