#!/usr/bin/env python

import argparse


def main():

    # parse CLI args
    parser = argparse.ArgumentParser(description="Computes profit/loss of a PokerStars HomeGame.")
    parser.add_argument("-b", "--buy-in", type=float, default=5, help="buy in (€)")
    parser.add_argument("players", metavar="PLAYER BALANCE", nargs="*", help="player names with chip balances")
    args = parser.parse_args()
    if len(args.players) % 2 != 0:
        parser.error("odd number of player arguments")

    # parse players and balances
    players = [args.players[k] for k in range(0, len(args.players), 2)]
    balances = [int(args.players[k+1]) for k in range(0, len(args.players), 2)]

    # compute profits
    profits = []
    for player, balance in zip(players, balances):
        profit = balance / sum(balances) * len(players) * args.buy_in - args.buy_in
        profits.append(profit)
    zero = sum(profits)

    # sort by profit
    profits, players, balances = zip(*sorted(zip(profits, players, balances), reverse=True))

    # print profits
    print("PokerStars HomeGame Calculator")
    print("==============================")
    for player, balance, profit in zip(players, balances, profits):
        print(f"{profit:+.2f}€ {player} ({balance})")
    print("------------------------------")
    print(f"{zero:+.2f}€")


if __name__ == "__main__":

    main()
