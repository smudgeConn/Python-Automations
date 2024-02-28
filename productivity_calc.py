import math

sessions = int(input("\n How many 30 minute sessions did you complete? "))
productivity = 70

def prod_calc(sessions, productivity):
        direct_minutes = sessions*30
        indirect_minutes = (math.floor(((direct_minutes*100) / productivity) - direct_minutes))/60

        return indirect_minutes

print(prod_calc(sessions, productivity))
