marvelchars= {
"Starlord":
  {"real name": "peter quill",
  "power": "dance moves",
  "archenemy": "Thanos"},

"Mystique":
  {"real name": "raven darkholme",
  "power": "shape shifter",
  "archenemy": "Professor X"},

"Hulk":
  {"real name": "bruce banner",
  "power": "super strength",
  "archenemy": "Adrenaline"}
             }
char_name=input("Which character do you want to know about? (Starlord, Mystique, Hulk) >>\n")#.lower().capitalize()  <--- this would work too 
char=char_name.lower().capitalize()
char_stat=input("Which statistic do you want to know about? (real name, power, archenemy) >>\n"
)
if char_stat=='real name':
    name=char_stat.title()
    
    print(f"{char}'s {char_stat} is {marvelchars.get(char, '').get(char_stat, '').title()}.\n")
    #{} in first bracket of .get and in the last one put char_
elif char_stat=='power' or 'archenemy':
    print(f"{char}'s {char_stat} is {marvelchars.get(char).get(char_stat)}.\n")
else:
    print("Invalid input.")