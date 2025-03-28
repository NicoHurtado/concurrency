
import threading
import random

lock = threading.Lock()

threads = []

def lazy_return_random_attacks():

    attacks = {"kimura": "upper_body",
               "straight_ankle_lock":"lower_body",
               "arm_triangle":"upper_body",
               "keylock": "upper_body",
               "knee_bar": "lower_body"}

    while True:
        with lock:
            random_attack = random.choice(list(attacks.keys()))

        yield random_attack

def thread_function(thread_id):

    attacks = lazy_return_random_attacks()

    for i in range(10):
        attack = next(attacks)
        print(f"Thread {thread_id}: {attack}")

for i in range(5):
    thread = threading.Thread(target=thread_function, args=(i,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()