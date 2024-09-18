print("Hello, World!")
js = int(input("are you woman?"))
p_today = int(input("today"))
p_month = int(input("month"))
if js == 0:
    print("sorry")
elif p_today > 2000 or p_month >= 20000 :
    print("congrats")
else:
    print("must",2001 - p_today)
    print("must", 20000 - p_month)
