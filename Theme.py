import random

Themes={
    # "name":{"bg":(),"ax":(),"pen":()}
    "GreenJeans":{"bg":(24,77,71),"ax":(214,239,199),"pen":(250,213,134)},
    "Candy":{"bg":(205,255,252),"ax":(255,199,100),"pen":(255,87,127)},
    "DarkAndYello":{"bg":(2,44,67),"ax":(17,81,115),"pen":(255,215,0)}
}

randomTheme={"bg":(random.randint(0,255),random.randint(0,255),random.randint(0,255)),
             "ax":(random.randint(0,255),random.randint(0,255),random.randint(0,255)),
             "pen":(random.randint(0,255),random.randint(0,255),random.randint(0,255)),
             }

