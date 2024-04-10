from random import choice
import random

def gen_password(tab, config, exclude):
    password = ""
    if any(tab[i] for i in range(0, 4)):
        for _ in range(tab[4]):
            rd_nb = choice([i for i in range(0,4) if i not in exclude])
            print(rd_nb)
            list = config[rd_nb] 
            rd_nb = random.randint(0, len(list) - 1) 
            val = list[rd_nb] 
            password = password + val

        return password
    ## Case where all is False
    else: return "Password can't be generated without minimum one option"
