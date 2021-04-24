import time
import math
from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini')

# read the base params from the config file
a = int(config.get('processing', 'a'))
b = int(config.get('processing', 'b'))
d = int(config.get('processing', 'd'))


def minJumps(a, b, d):
    # Base case: when source and
    # destination are same
    if a == b:
        return 0

    # when nothing is reachable
    # from the given fixed step distance
    if d == 0:
        return float('inf')

    minSteps = math.ceil((b - a) / d)

    return minSteps


if __name__ == "__main__":

    if a > b:
        print("a can't be > b. Please enter new values")
    else:
        print('Minimum number of jumps to reach',
              'end is', minJumps(a, b, d))
