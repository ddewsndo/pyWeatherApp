import requests

API_KEY = '9a77dbe6a1c28e3e8a5c8c085c45c3a7'
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

print("\n\nHi! Welcome to my weather app. Enter a city you would like to know the weather for!\n")

while True:
        units = input("Would you like information in Fahrenheit or Celsius? (type F or C):  ")
        if units.lower().strip() == "c":
            chosenUnits = "metric"
            tempInitial = "C"
            break
        elif units.lower().strip() == "f":
            chosenUnits = "imperial"
            tempInitial = "F"
            break
        else:
            print("Incorrect input, type only C or F.\n")

while True:

    userCity = input("\nEnter city: (or type quit to exit) ")

    if userCity.lower().strip() == "quit":
        break

    #1 build the URL using f string
    url = f"{BASE_URL}?q={userCity}&appid={API_KEY}&units={chosenUnits}"

    #2 send the GET request
    response = requests.get(url)

    #3 check if request was successful
    if response.status_code == 200:
        #4turn the reponse into JSON (python dict)
        data = response.json()

        #5 extract data if want
        temperature = data['main']['temp']
        description = data['weather'][0]['description']

        #6 print
        print(f"\n\nWeather in {userCity.title()}:")
        print(f"Temperature: {temperature} {tempInitial}")
        print(f"Condition: {description}\n\n")
    else:
        print(f"Sorry, Couldn't find the city, check spelling and try again.")
    
    