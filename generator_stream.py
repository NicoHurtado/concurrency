import time
import random

# Stream simulation class
class AttackStream:
    def __init__(self):
        self.attacks = {"kimura": "upper_body",  
                       "straight_ankle_lock":"lower_body",
                       "arm_triangle":"upper_body",
                       "keylock": "upper_body",
                       "knee_bar": "lower_body"}
        
    def get_attacks(self, num_attacks=10, delay=1):
        for _ in range(num_attacks):
            attack = random.choice(list(self.attacks.keys()))
            time.sleep(delay)
            yield attack
                      
def process_attacks(attack_stream):
    for attack in attack_stream:
        print(f"Received attack: {attack}")
        
stream = AttackStream()

process_attacks(stream.get_attacks(10, 1))