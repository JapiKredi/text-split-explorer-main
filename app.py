def get_greeting(name):
    return f"Hi {name}"


message = get_greeting("Jasper")
file = open("contact.txt",'w')
file.write(message)
