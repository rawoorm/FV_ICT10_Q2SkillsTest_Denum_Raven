
from pyscript import document

elements = {
    "H": ('HYDROGEN', 'H', 1, 1.008),
    "HE": ('HELIUM', 'He', 2, 4.0026),
    "C": ('CARBON', 'C', 6, 12.011),
    "N": ('NITROGEN', 'N', 7, 14.007),
    "O": ('OXYGEN', 'O', 8, 15.999),
    "F": ('FLUORINE', 'F', 9, 18.998),
    "NE": ('NEON', 'Ne', 10, 20.180),
    "P": ('PHOSPHORUS', 'P', 15, 30.974),
    "S": ('SULFUR', 'S', 16, 32.06),
    "CL": ('CHLORINE', 'Cl', 17, 35.45),
    "AR": ('ARGON', 'Ar', 18, 39.948),
    "SE": ('SELENIUM', 'Se', 34, 78.971),
    "BR": ('BROMINE', 'Br', 35, 79.904),
    "KR": ('KRYPTON', 'Kr', 36, 83.798),
    "I": ('IODINE', 'I', 53, 126.904),
    "XE": ('XENON', 'Xe', 54, 131.293),
    "RN": ('RADON', 'Rn', 86, 222)
}


# Function to search your element
def search_element(e):

    # Get the input from HTML
    element1 = document.getElementById("element1").value.strip().upper()

    # Retrieve information from the dictionary
    result = elements.get(
        element1,
        ('Element not found', '-', '-', '-')
    )

    # Display the result in HTML
    document.getElementById("element").innerText = result[0]
    document.getElementById("symbol").innerText = result[1]
    document.getElementById("atomicnumber").innerText = result[2]
    document.getElementById("atomicmass").innerText = result[3]
