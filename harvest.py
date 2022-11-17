############
# Part 1   #
############


class MelonType:
    """A species of melon at a melon farm."""

    def __init__(
        self, code, first_harvest, color, is_seedless, is_bestseller, name
    ):
        """Initialize a melon."""

        self.pairings = []
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name


        # Fill in the rest

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""
        
        self.pairings.append(pairing)
        

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code
        


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    musk = MelonType(
        "musk",
        1998,
        "green",
        True,
        True,
        "Muskmelon"
    )
    musk.add_pairing("mint")

    cas = MelonType(
        "cas",
        2003,
        "orange",
        False,
        False,
        "Casaba"
)
    cas.add_pairing("mint")
    cas.add_pairing("strawberry")

    cren = MelonType(
        "cren",
        1996,
        "green",
        False,
        False,
        "Crenshaw"
)
    cren.add_pairing("prosciutto")

    yw = MelonType(
        "yw",
        2013,
        "yellow",
        True,
        True,
        "Yellow Watermelon"
    )
    yw.add_pairing("ice cream")
   
    all_melon_types.append(musk)
    all_melon_types.append(cas)
    all_melon_types.append(cren)
    all_melon_types.append(yw) 
    return all_melon_types
    

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings.
    Muskmelon pairs with
    - mint
    """

    for object in melon_types:
        print(f"{object.name} pairs with")
        for pair in object.pairings:
            print(f"- {pair}")


# ls = make_melon_types()
# print_pairing_info(ls)


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""
    dtc = {}

    #melon_types = [4 objects]
    for object in melon_types:
        dtc[object.code] = object.name

    return dtc
    
# ls = make_melon_types()
# make_melon_type_lookup(ls)

############
# Part 2   #
############


class Melon:
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods
    def __init__(self, type, shape, color_ratings, field, farmer):
        self.type = type
        self.shape = shape
        self.color_ratings = color_ratings
        self.field = field
        self.farmer = farmer

    def is_sellable(self):
        if (self.shape > 5 and self.color_ratings > 5 and self.field != 3):
            return True
        return False


def make_melons(melon_types):
    """Returns a list of Melon objects."""

    list_of_melons = []

    melons_by_id = make_melon_type_lookup(melon_types) # a dictionanry {'musk': 'Muskmelon', 'cas': 'Casaba', 'cren': 'Crenshaw', 'yw': 'Yellow Watermelon'}

    melon_1 = Melon(melons_by_id['yw'], 8, 7, 2, 'Sheila')
    melon_2 = Melon(melons_by_id['yw'], 3, 4, 2, 'Sheila')
    melon_3 = Melon(melons_by_id['yw'], 9, 8, 3, 'Sheila')
    melon_4 = Melon(melons_by_id['cas'], 10, 6, 35, 'Sheila')
    melon_5 = Melon(melons_by_id['cren'], 8, 9, 35, 'Michael')
    melon_6 = Melon(melons_by_id['cren'], 8, 2, 35, 'Michael')
    melon_7 = Melon(melons_by_id['cren'], 2, 3, 4, 'Michael')
    melon_8 = Melon(melons_by_id['musk'], 6, 7, 4, 'Michael')
    melon_9 = Melon(melons_by_id['yw'], 7, 10, 3, 'Sheila')

    ist_of_melons = [melon_1, melon_2, melon_3, melon_4, melon_5, melon_6, melon_7, melon_8, melon_9]

    return ist_of_melons

# ls = make_melon_types()
# print(make_melons(ls))


def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""
    # Harvested by Sheila from Field 2 (CAN BE SOLD)
    for melon in melons:
        if melon.is_sellable() == True:
            print(f"Harvested by {melon.farmer} from Filed {melon.field} (CAN BE SOLD)")
        else:
            print(f"Harvested by {melon.farmer} from Field {melon.field} (NOT SELLABLE)")

# ls1 = make_melon_types()    
# ls2 = make_melons(ls1)
# get_sellability_report(ls2)
