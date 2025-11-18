# write code to implement a turnstile
state = "locked"
checks = {
"unlocked" : {"push":"locked","coin":"coin rejected","quit":"you can't quit right now"},
"locked" : {"push":"nothing happens","coin":"unlocked","quit":"quit"}}
while True:
    inp = ""
    while inp != "coin" and inp !="push" and inp!="quit":
        inp = (input(f"The turnstile is {state}. You can push or coin.(you may use \"quit\" if it is locked) ")).lower()
    key = str(checks[state][inp])
    if(key == "locked" or key == "unlocked"):
        state = key
    elif(key == "quit"):
        quit()
    else:
        print(key)
    