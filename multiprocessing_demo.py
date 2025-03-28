import multiprocessing
import random
import os

def lazy_return_random_attacks(lock):
    attacks = {
        "kimura": "upper_body",
        "straight_ankle_lock": "lower_body",
        "arm_triangle": "upper_body",
        "keylock": "upper_body",
        "knee_bar": "lower_body"
    }

    while True:
        with lock:
            random_attack = random.choice(list(attacks.keys()))
        yield random_attack

def print_attacks(args):
    num, lock = args
    attacks = lazy_return_random_attacks(lock)
    for _ in range(num):
        attack = next(attacks)
        print(f"Process {os.getpid()}: {attack}")

if __name__ == '__main__':
    multiprocessing.set_start_method('spawn')
    with multiprocessing.Manager() as manager:
        lock = manager.Lock()
        with multiprocessing.Pool(processes=2) as pool:
            pool.map(print_attacks, [(3, lock)] * 2)
