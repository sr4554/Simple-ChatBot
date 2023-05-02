import random

R_JOKE="One joke, coming up! What is a sea monster’s favorite snack? Ships and dip"
R_WEATHER="I think its quite sunny"


def unknown():
    response=['Could you please re-phrase that?',
              "....."
              "I am not sure",
              "What does that mean?"
              "I am not that advanced I'am just a simple bot"][random.randrange(5)]
    return response