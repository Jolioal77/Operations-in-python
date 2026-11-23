print("===Smart School Day Planner===")
print("Answer 3 quick questions and I will plan your day!\n")

day = input("What day is it? (Monday to Sunday):").strip().capitalize()
weather = input("What is the weather? (Sunny / rainy / cloudy):").strip().lower()
homework = input("Is your homework done? (yes / no):").strip().lower()

print()
print(f"===Your Plan for {day}===")
print("_"*35)

if day in ("Saturday", "Sunday"):
    print("Day type: Weekend - enjoy your free time!")
elif day == "Monday":
    print("Day type: First day of the week, Pack your weekly planner.")
elif day == "Friday":
    print("Day type: Last school day. Return library books today.")
elif day in ("Tuesday", "Wednesday", "Thursday"):
    print("Day type: Regular school day, stay focused!")
else:
    print("Day type: Day not recognized, Please check spelling")



if weather == "sunny" and homework == "yes":
    print("After school: Head to park - great weather and homework is done!")

if weather == "rainy" or weather == "cloudy":
    print("Weather tip: Pack your umbrella it might rain.")

if not (homework == "yes"):
    print("Homework: Not done yet, finish it before you go out!")

if weather == "rainy" and not (homework == "yes"):
    print("After school stay home and finish your homework, it's rainy outside!")
elif weather == "sunny" and homework == "yes" and not(day in ("Saturday", "Sunday")):
    print("All set for a great school day! Enjoy the sunshine after school!")
elif day in ("Saturday", "Sunday") and weather == "sunny":
    print("Best plan: perfect weekend have fun outside! ")
else: print("Best plan is to take it easy and enjoy your day!")

print("Plan has been completed! Have a great day!")