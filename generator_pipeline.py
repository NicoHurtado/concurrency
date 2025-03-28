import time
import random

def attack_stream():
    attacks = ["kimura", "ankle_lock", "triangle"]
    while True:
        yield random.choice(attacks)
               
def log_attacks(stream):
    for attack in stream:
        print(f"Logging attack: {attack}")
        yield attack
        
def counter_attacks(stream):
    for attack in stream:
        if attack == "kimura":
            print(f"Countering kimura attack!") 
        yield attack
        
stream = attack_stream() 
stream = log_attacks(stream)
stream = counter_attacks(stream)

for _ in range(10):
    next(stream)