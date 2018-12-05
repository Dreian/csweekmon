"""The implementation of the Counter move.

It is a slightly stronger version of Tackle. Its effectiveness increases if you just received a
significant amount of damage.
"""

import random
from utils import delay_ui, print_ui

NAME = 'Counter'
PP_COST = 5
SUCCESS_RATE = 90
CRIT_RATE = 20

def perform(user, other):
    """Perform Counter."""
    if random.randint(0, 100) < SUCCESS_RATE:
        if random.randint(0, 100) < CRIT_RATE:
            print_ui('  It\'s super effective!')
            delay_ui(1)
            base_damage = max(0, user.stats['Recent damage'] + \
                    user.stats['Strength'] - 0.5 * other.stats['Defense'])
        else:
            base_damage = max(0, 0.5 * user.stats['Recent damage'] + \
                    user.stats['Strength'] - other.stats['Defense'])
        damage = max(1, random.randint(int(0.8 * base_damage), int(1.2 * base_damage + 1)))
        if damage == 1:
            print_ui('  It deals {} point of damage.'.format(damage))
        else:
            print_ui('  It deals {} points of damage.'.format(damage))
        user.recent_damage = 0
        other.recent_damage = damage
        other.stats['HP'] -= damage
    else:
        print_ui('  It\'s ineffective!')