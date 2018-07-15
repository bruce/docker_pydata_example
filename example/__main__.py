import time
import random

from __init__ import State

state = State("/app/data/state.pkl")
state.append({
    'timestamp': time.time(),
    'value': random.randint(1, 100)
})
state.save()
print(state)
