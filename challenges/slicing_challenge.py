challenge= [
    "science", "turbo", 
    ["goggles", "eyes"], 
    "nothing"
    ]
# eyes goggles nothing
#My eyes! The goggles do nothing!
a=challenge[2][1]
b=challenge[2][0]
c=challenge[3]
print("Challenge level:")
print(f"My {a}! The {b} do {c}! \n")

trial= [
    "science", "turbo", 
    {"eyes": "goggles", "goggles": "eyes"}, 
    "nothing"
    ]
# eyes goggles nothing
#My eyes! The goggles do nothing!
print("Trial level:")
d=trial[2].get("goggles")
e=trial[2].get("eyes")
f=trial[3]
print(f"My {d}! The {e} do {f}! \n")

nightmare= [{
    "slappy": "a", 
    "text": "b", 
    "kumquat": "goggles", 
    "user":{
        "awesome": "c", 
        "name": {
            "first": "eyes", 
            "last": "toes"
            }},
    "banana": 15, 
    "d": "nothing"
    }]
# eyes goggles nothing
#My eyes! The goggles do nothing!
g=nightmare[0].get("user").get("name").get("first")
h=nightmare[0].get("kumquat")
i=nightmare[0].get("d")
print("Nightmare level:")
print(f"My {g}! The {h} do {i}!")