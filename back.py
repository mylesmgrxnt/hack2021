def automotive_carbon(t,miles,make=None):
    c = [0.536,0.222,0.882,0.544]
    if t == "bus":
        pollution = miles*c[0]
    elif t == "train":
        pollution = miles*c[1]
    elif t == "car":
        if make == "gas":
            pollution = miles*c[2]
        elif make == "hybrid":
            pollution = miles*c[3]
        elif make == "electric":
            pollution = 0
    return round(pollution,1)
'''
def home_carbon(state,cost):
    with open("states.csv") as f:
        for line in f:
            a = line.split(',')
            print(a)
            if a[0] == state:
                print("yes")
'''