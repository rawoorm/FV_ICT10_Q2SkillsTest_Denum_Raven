from pyscript import document 

planets = {"MERCURY": ('Mercury', 1, 0),
           "VENUS": ('Venus', 2, 0)}

#function to search your planet
def search_planet(e):
    # Get the input from HTML

    planet1 = document.getElementById("planet1").value.upper()
    # retrieve info from the dictionary
    result = planets.get(planet1,('Planet not found', "-", "-"))
    # display the result in HTML
    document.getElementById("code").innerText = planet1
    document.getElementById("name").innerText = result[0]
    document.getElementById("order").innerText = result[1]
    document.getElementById("moons").innerText = result[2]

