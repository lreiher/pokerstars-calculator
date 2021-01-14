#!/usr/bin/env python

import sys

bet = 5

names = sys.argv[1::2]
chips = [int(c) for c in sys.argv[2::2]]

nplayers = len(names)

profits = {}
for n, c in zip(names, chips):
  profits[n] = c / sum(chips) * nplayers * bet - bet
balance = sum(profits.values())

print("Profits")
print("===============")
for n, p in profits.items():
  print(f"{p:+.2f}€ {n}")
print("===============")
print(f"{balance:+.2f}€")
