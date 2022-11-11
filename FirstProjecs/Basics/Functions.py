def print_hi(name):
    """Print HI"""
    print("Congratulations " + name + " wish you all the best!")

print_hi("Jeka")

#########################################

def summa(x, y):
    print(x+y)

summa(1,5)

########################################

def summa1(x, y):
    return x+y
b = summa1(2, 7)
print(b)

#######################################

def create_record(name, telephone, address):
    """Create record"""
    record = {
        'name': name,
        'phone': telephone,
        'address': address
    }
    return record

user1 = create_record("Bob", "0990674329", "Alicante")
user2 = create_record("Tolik", "0630674329", "Odessa")

print(user1)
print(user2)

#########################################

def give_award(medal, *persons): # * значит много
    """Give Medals to persons"""
    for person in persons:
        print("Mr. " + person.title() + " is award " + medal)


give_award("PornoHero", "Bob", "Victor") # * "Bob", "Victor"

