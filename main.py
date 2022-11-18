class Human:
    height = 170
    satiety = 50
class Local_men(Human):
    satiety = 0
class Local_women(Human):
    satiety = 100
Local_toilet_enjoyer = Local_women
Local_shower_fan = Local_men
print("Local toilet enjoyer height =", Local_toilet_enjoyer.height)
print("Local shower crapper height =", Local_shower_fan.height)
print("human not hungry meter = ", Human.satiety, "level")
print("Local women hungry meter = ",Local_women.satiety, "level")
print("Local men hungry meter = ",Local_men.satiety, "level")