#!/usr/bin/env python
# -*-coding:utf-8-*-
from time import sleep
import random

sep = "-"*35


"""
    Diccionario:
    La key("piedra") le gana a los valores dentro de ella("lagarto tijera")
"""
dic = { 
        "piedra": "lagarto tijera",
        "papel": "piedra spock",
        "tijera": "papel lagarto",
        "spock": "tijera piedra",
        "lagarto": "spock papel"
    }

keys = [i for i in dic.keys()]

def think():
    print(".")
    sleep(0.5)
    print(".")
    sleep(0.5)
    print(".")
    sleep(0.4)

while True:
    # raw_input() en python2
    user_choice = input("Elige piedra, papel, tijera, spock o lagarto: ")
    
    if user_choice not in dic:
        print ("No hagas trampa!")
        continue

    pc_choice = random.choice(keys)
    think()
    print (("\nLa Computadora elijio {}.").format(pc_choice, user_choice))
    think()

    if user_choice == pc_choice:
        print (("\nEmpate.\n{}").format(sep))
    
    elif pc_choice in dic[user_choice]:
        print (("\nGanaste. {} gana a {}\n{}").format(user_choice, pc_choice, sep))
    else:
        print (("\nPerdiste. {} gana a {}\n{}").format(pc_choice, user_choice, sep))

input()
