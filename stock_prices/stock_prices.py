#!/usr/bin/python

import argparse


def find_max_profit(prices):
    # make variables for current_min_price_so_far and max_profit_so_far
    cur_min = 0
    max_profit = [] # <----- we make this an array of all the profits and then find largest one. Thanks Ethan from help channel lol

    # To fill the max profit, we now need to set the cur_min and compare to each element in the array. Finding each profit.
    for i in range(0, len(prices) - 1):
        cur_min = prices[i]

        for j in range(i+1, len(prices) -1):
            max_profit.append(prices[j] - cur_min) # <---- This will give us all the potential profits into one list
    
    return max(max_profit)



if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
