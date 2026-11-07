
from pyscript import document, when

# Dictionary containing the non-metal elements
# Each element has its name, symbol, atomic number, and atomic mass
elements = {
    "H": ('HYDROGEN', 'H', 1, 1.008),
    "He": ('HELIUM', 'He', 2, 4.0026),
    "C": ('CARBON', 'C', 6, 12.011),
    "N": ('NITROGEN', 'N', 7, 14.007),
    "O": ('OXYGEN', 'O', 8, 15.999),
    "F": ('FLUORINE', 'F', 9, 18.998),
    "Ne": ('NEON', 'Ne', 10, 20.180),
    "P": ('PHOSPHORUS', 'P', 15, 30.974),
    "S": ('SULFUR', 'S', 16, 32.06),
    "Cl": ('CHLORINE', 'Cl', 17, 35.45),
    "Ar": ('ARGON', 'Ar', 18, 39.948),
    "Se": ('SELENIUM', 'Se', 34, 78.971),
    "Br": ('BROMINE', 'Br', 35, 79.904),
    "Kr": ('KRYPTON', 'Kr', 36, 83.798),
    "I": ('IODINE', 'I', 53, 126.904),
    "Xe": ('XENON', 'Xe', 54, 131.293),
    "Rn": ('RADON', 'Rn', 86, 222)
}


# Function that runs when the search button is clicked
# The button is identified by its HTML ID: search-btn
@when("click", "#search-btn")
def search_element(event):

    # Get the user's input from the HTML text box
    # strip() removes unnecessary spaces
    # upper() converts the input into uppercase
    element1 = document.getElementById("element1").value.strip().capitalize()

    # Search for the entered symbol in the elements dictionary
    # If the symbol does not exist, display "Element not found"
    result = elements.get(
        element1,
        ('Element not found', '-', '-', '-')
    )

    # Display the element name in the HTML
    document.getElementById("element").innerText = result[0]

    # Display the chemical symbol in the HTML
    document.getElementById("symbol").innerText = result[1]

    # Display the atomic number in the HTML
    document.getElementById("atomicnumber").innerText = str(result[2])

    # Display the atomic mass in the HTML
    document.getElementById("atomicmass").innerText = str(result[3])

