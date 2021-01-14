# PokerStars Calculator

This tool calculates profit/loss of a [PokerStars HomeGame](https://www.pokerstars.eu/de/poker/home-games/).

The total number of chips within the game is continually decreasing, since the software/bank takes a cut.

### Usage

```
❯ ./poker.py --help
usage: poker.py [-h] [-b BUY_IN] [PLAYER BALANCE ...]

Computes profit/loss of a PokerStars HomeGame.

positional arguments:
  PLAYER BALANCE        player names with chip balances

optional arguments:
  -h, --help            show this help message and exit
  -b BUY_IN, --buy-in BUY_IN
                        buy in (€)
```
