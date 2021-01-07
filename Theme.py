import random

Themes={
    # "name":{"bg":(),"ax":(),"pen":()}
    "Dark":{"bg":(2,44,67),"ax":(48,71,94),"pen":(240,84,84)},
    "GreenJeans":{"bg":(24,77,71),"ax":(214,239,199),"pen":(250,213,134)},
    "Candy":{"bg":(205,255,252),"ax":(255,199,100),"pen":(255,87,127)},
    "DarkAndYellow":{"bg":(2,44,67),"ax":(17,81,115),"pen":(255,215,0)},
    "Girly":{"bg":(255,123,84),"ax":(255,213,107),"pen":(147,155,98)},
    "CyberPunk":{"bg":(17,29,94),"ax":(243,113,33),"pen":(192,226,24)},
    "Lavender":{"bg":(88,61,114),"ax":(159,95,128),"pen":(255,142,113)},
    "Rose":{"bg":(216,172,156),"ax":(239,217,209),"pen":(244,238,237)},
    "Sky":{"bg":(25,69,107),"ax":(17,105,142),"pen":(22,199,154)}
}

randomTheme={"bg":(random.randint(0,172),random.randint(0,172),random.randint(0,172)),
             "ax":(random.randint(100,172),random.randint(100,172),random.randint(100,172)),
             "pen":(random.randint(172,255),random.randint(172,255),random.randint(172,255)),
             }