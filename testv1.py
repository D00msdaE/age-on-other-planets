userAge = int(input(f'How old are you: '))
print('Available planets are: ')
print("\n m = mecury \n v = venus \n e = earth \n ma = mars \n j = jupiter \n s = saturn \n u = uranus \n n = neptune \n p = pluto")
planet = str(input(f'Pick a planet:  '))

#planets oribital period. might convert it to a dictionary or tuple whatever later
mecuryYears = 0.240846
venusYears   = 0.615198
earthYears   = 1
marsYears    = 1.881
jupiterYears = 11.862
saturnYears  = 29.4571
uranusYears  = 84.0205
neptuneYears = 164.8
plutoYears   = 248.1

# planet chooser checker (input checking)
if planet == 'm':
	planet = 'mecury'
	mecuryAge = userAge / mecuryYears
	age = mecuryAge
elif planet == 'v':
	planet = 'venus' 
	venusAge = userAge / venusYears
	age = venusAge
elif planet == 'e':
	planet = 'earth'
	earthAge = userAge / earthYears
	age = earthAge
elif planet == 'ma':
	planet = 'mars'
	marsAge = userAge / marsYears
	age = marsAge
elif planet == 'j':
	planet = 'jupiter'
	jupiterAge = userAge / jupiterYears
	age = jupiterAge
elif planet == 's':
	planet = 'saturn'
	saturnAge = userAge / saturnYears
	age = saturnAge
elif planet == 'u':
	planet = 'uranus'
	uranusAge = userAge / uranusYears
	age = uranusAge
elif planet == 'n':
	planet = 'neptune'
	neptuneAge = userAge / neptuneYears
	age = neptuneAge
elif planet == 'p':
	planet = 'pluto'
	plutoAge = userAge / plutoYears
	age = plutoAge
else:
	print(f'Please input a valid character.')
	
print(f'You are {age} years old on {planet}.')
