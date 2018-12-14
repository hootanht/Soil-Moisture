

# Data Of Plant
shaghayegh = 1
roz = 2
sefid = 3

# Data Of Location
garm = 1
sard = 2
motadel = 3

#Method Of Chose Plant
def FinalUserPlant(plant):
    if plant.lower() == "1" or plant.lower() == "shaghayegh":
        return "shaghayegh"
    elif plant.lower() == "2" or plant.lower() == "roz":
        return "roz"
    elif plant.lower() == "3" or plant.lower() == "sefid":
        return "sefid"
    else:
        return "null"

#Method Of Chose Locaion
def FinalUserLocation(location):
    if location.lower() == "1" or location.lower() == "garm":
        return "garm"
    elif location.lower() == "2" or location.lower() == "sard":
        return "sard"
    elif location.lower() == "3" or location.lower() == "motadel":
        return "motadel"
    else:
        return "null"
        
#Method Of Soil Moisture
def FinalUserSoilMoisture(soilMositure):
    if type(soilMositure) is int :
        return soilMositure
    else:
        return "null"

#Method Of Calculate Plant Mode
def PlantMode(plant,location,solidMoisture):
    #Get Plant Number
    plantnumber = 0
    if plant == "shaghayegh":
        plantnumber = 1
    elif plant == "roz":
        plantnumber = 2
    elif plant == "sefid":
        plantnumber = 3
    else:
        print("Can't Calculate")
    #Get Location Number
    locationnumber = 0
    if location == "garm":
        locationnumber = 1
    elif location == "sard":
        locationnumber = 2
    elif location == "motadel":
        locationnumber = 3
    else:
        print("Can't Calculate")
    #Get Soil Moisture Number
    soilmoisturenumber = 0
    if type(solidMoisture) is int:
        soilmoisturenumber = solidMoisture
    else:
        print("Can't Calculate")
    if plantnumber != 0 and locationnumber != 0 and soilmoisturenumber != 0:
        plantMode = plantnumber*locationnumber*soilmoisturenumber
        print("\n" + str(plantMode) +"\n")
        if plantMode<10 :
            print("Your Plant Soil Moisture Is Low!")
        elif plantMode>20:
            print("Your Plant Soil Moisture Is High!")
        else:
            print("Your Plant Soil Moisture Is Very Good!")
    else:
        print("The Number Is Not Vaild")


while True:
    userPlant = input("Please Select Your Plant : \n 1)Shaghayegh \n 2)Roz \n 3)Sefid \n")
    finaluserplant = FinalUserPlant(userPlant)
    if finaluserplant == "shaghayegh" or finaluserplant == "roz" or finaluserplant == "sefid":
        userLocation = input(
        "Your Plant Is {} , Now Please Select Your Location : \n 1)Garm \n 2)Sard \n 3)Motadel \n".format(finaluserplant))
        finaluserlocation = FinalUserLocation(userLocation)
        if finaluserlocation == "garm" or finaluserlocation == "sard" or finaluserlocation == "motadel":
            userSoilMoisture = int(input("Your Plant Is {} And Your Location Is {} , Now Enter The Soil Moisture : \n".format(finaluserplant,finaluserlocation)))
            finalusersoilmoisture = FinalUserSoilMoisture(userSoilMoisture)
            if type(finalusersoilmoisture) is int:
                PlantMode(finaluserplant,finaluserlocation,finalusersoilmoisture)
            else:
                print("Please Select The Right Option!!!")
        else:
            print("Please Select The Right Option!!!")
    else:
        print("Please Select The Right Option!!!")
    continuereq = input("Do You Want To Try Again ? (Y/N)")
    if continuereq.lower() == "y":
        pass
    elif continuereq.lower() == "n":
        break
    else:
        print("Invalid Entries , StartOver...")





