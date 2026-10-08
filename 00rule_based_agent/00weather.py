weather = input("What is the weather like today? ")

if weather.lower() == "rain":
    print("Take an umbrella!")

elif weather.lower() == "sun":
    print("Wear sunglasses!")

elif weather.lower() == "snow":
    print("Wear a coat!")

elif weather.lower() == "cloudy":
    print("It might be a bit gloomy today.")

elif weather.lower() == "windy":
    print("Hold onto your hat!")

else:
    print("Have a nice day!")