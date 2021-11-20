# A time traveler has suddenly appeared in your classroom!

# Create a variable representing the traveler's
# year of origin (e.g., year = 2000)
# and greet our strange visitor with a different message
# if he is from the distant past (before 1900),
# the present era (1900-2020) or from the far future (beyond 2020).

year = int(input("Greetings! What is your year of origin? ")) #Added parenthesis after 'int' and double quotes after 'origin?' and changed '==' to '=' 

if year <= 1900:  #added ':' after 1900
    print ("Woah, that's the past!") #added double quotes
elif year > 1900 and year < 2021: #replaced '&&' with 'and'
    print ("That's totally the present!")
else: #replaced 'elif' with else
    print ("Far out, that's the future!!")
