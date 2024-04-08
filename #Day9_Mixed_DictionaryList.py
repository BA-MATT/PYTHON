country = input("Please enter country name: ") # Add country name
visits = int(input("Please enter number of cities visited: ")) # Number of visits
list_of_cities = eval(input("Please enter city name: ")) # create list from formatted string

travel_log = [
  {
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
  },
  {
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
  },
]
# Do NOT change the code above 👆

# TODO: Write the function that will allow new countries
# to be added to the travel_log. 
def add_new_country (country, visits,list_of_cities):
    new_country={}
    new_country["country"]=country
    new_country["visits"]=visits
    new_country["citiess"]=list_of_cities  #KEY should be the same
    travel_log.append(new_country)
    print(travel_log)


# Do not change the code below 👇
add_new_country(country, visits, list_of_cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['citiess'][0]}.") #KEY should be the same