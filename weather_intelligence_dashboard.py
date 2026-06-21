# Weather Intelligence Dashboard

import requests

while True:
      print('1) Search Weather')
      print('2) Search History')
      print('3) Exit')
      try:
          option = int(input('Please enter a number option:'))
    
          if option == 1:
                try:
                    city  = input('Please enter the city: ')
                    url  =  f"https://wttr.in/{city}?format=j1"
                    response = requests.get(url)
                    data = response.json()
                    temperature = data["current_condition"][0]["temp_C"]
                    condition = data["current_condition"][0]["weatherDesc"][0]["value"]
                    print("\nWeather Dashboard")
                    print("City:", city)
                    print("Temperature:", temperature, "°C")
                    print("Condition:", condition)
                    with open("weather_history.txt", "a") as file:
                         file.write(city + "\n")
                except:
                    print('Please enter a valid city name or check your internet connection')
          elif option == 2:
                 try:
                     with open ("weather_history.txt", 'r') as file:
                          content = file.read()
                     print(content)
                 except FileNotFoundError:
                         print("No search history found yet.")
          elif option == 3:
               print('Thank you. Good Bye')
               break
          else:
              print('Invalid option')
      except ValueError:
             print('Please Enter a valid number for the option')
          

        
              