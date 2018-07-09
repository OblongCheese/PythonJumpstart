import os
import csv

# how to handle importing modules that may not be available in older python releases
try:
    import statistics
except:
    import youtry.statistics_standin_for_py2 as statistics

from you_try.data_types import Purchase


def main():
    print_header()
    filename = get_data_file()
    data = load_file(filename)
    query_data(data)


def print_header():
    print('---------------------------------------------')
    print('--------------Real Estate App----------------')
    print('---------------------------------------------')


def get_data_file():
    base_folder = os.path.dirname(__file__)
    return os.path.join(base_folder, 'data', 'SacramentoRealEstateTransactions2008.csv')


# def load_file_basic(filename):
#    with open(filename, 'r', encoding='utf-8') as fin:
#        header = fin.readline().strip()
#        print('found header: ' + header)
#
#        lines = []
#        for line in fin:
#            line_data = line.strip().split(',')
#            lines.append(line_data)
#
#        print(lines[:5])
#
#    return []

def load_file(filename):
    with open(filename, 'r', encoding='utf-8') as fin:
        reader = csv.DictReader(fin)
        purchases = []
        for row in reader:
            p = Purchase.create_from_dict(row)
            purchases.append(p)

    return purchases


def get_price(p):
    return p.price


def query_data(data):
    # if data was sorted by price:
    # data.sort(key=get_price)

    # instead of defining an function exteranl to this one, we can use lambda functions to do basic operations
    # e.g return a value from a class, do basic math, etc

    # the following calls the sort function built in to all lists and sorts based on the price attribute of the
    # instantiations of the Purchase classes contained within the list
    data.sort(key=lambda p: p.price)

    # most expensive house?
    high_purchase = data[-1]
    print("The most expensive house is: ${:,} with {} beds and {} bathrooms.".format(high_purchase.price,
                                                                                     high_purchase.beds,
                                                                                     high_purchase.baths))

    # lease expensive house?
    low_purchase = data[0]
    print("The least expensive house is: ${:,} with {} beds and {} bathrooms.".format(low_purchase.price,
                                                                                      low_purchase.beds,
                                                                                      low_purchase.baths))

    # average price of all homes
    # prices = []
    # for pur in data:
    #    prices.append(pur.price)

    prices = [
        # projection or items to create
        p.price
        # the set to process
        for p in data
    ]

    ave_price = statistics.mean(prices)
    print("The average home price is ${:,}".format(int(ave_price)))

    # average price of 2 bedroom house
    # prices = []
    # for pur in data:
    #    if pur.beds == 2:
    #        prices.append(pur.price)

    # create a list using list comprehensions
    two_bed_homes = [
        p  # projection or items to create
        for p in data  # the set to process
        if p.beds == 2  # test/condition
    ]

    # create a list using generator expressions
    # this expression will pull in more data every time it is called later in the file
    # the only difference between this and the above code is the container: square brackets above, parenthesis below
    # chain generator expressions together to create a data pipeline: at the end of a generator expression, call another
    two_bed_homes = (
        p  # projection or items to create
        for p in data  # the set to process
        if announce(p, "2-bedrooms, this has {}".format(p.beds)) and p.beds == 2  # test/condition
    )

    homes = []
    for h in two_bed_homes:
        if len(homes) > 5:
            break
        homes.append(h)

    ave_price = statistics.mean([announce(p.price, 'price') for p in homes])
    ave_baths = statistics.mean([p.baths for p in homes])
    ave_sq_ft = statistics.mean([p.sq__ft for p in homes])
    print("The average 2-bedroom home price is ${:,} with approx. {} bathrooms and total average size {} square foot."
          .format(int(ave_price), round(ave_baths, 1), round(ave_sq_ft, 1)))


def announce(item, msg):
    print("Evaluating item {} for condition {}".format(item, msg))
    return item


if __name__ == '__main__':
    main()
