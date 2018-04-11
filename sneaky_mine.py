#!/usr/bin/env python

import random

ALPHA = None


def sneaky_miner_gets_the_next_block():
    return random.random() <= ALPHA


def event1():
    if sneaky_miner_gets_the_next_block():
        return 3.0 - (1 + 2 * ALPHA)   # event1A, sneaky miner got 3 blocks published
    else:
        return 2.0 - (1 + ALPHA)  # event2A, sneaky miner got 2 blocks


def event2():
    if sneaky_miner_gets_the_next_block():
        return 2.0 - (1 + ALPHA)  # event2A, sneaky miner gets 2 blocks
    else:
        return -(1 + ALPHA)  # event2B, sneaky miner lost and gets 0 blocks


def mine():
    n = random.random()
    if n <= 0.1:  # event3
        return 0.0  # sneaky miner got zero advantage
    if sneaky_miner_gets_the_next_block():
        return event1()
    else:
        return event2()


def main():
    global ALPHA
    iterations = 2000000
    alpha_min = 0.0
    alpha_max = 0.51
    for _ in range(20):
        ALPHA = (alpha_min + alpha_max) / 2.0
        avg_blocks = sum(mine() for _ in xrange(iterations)) / float(iterations)
        print ALPHA, avg_blocks
        if avg_blocks > 0.0:
            alpha_max = ALPHA
        else:
            alpha_min = ALPHA


if __name__ == '__main__':
    main()