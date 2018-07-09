import journal

def main():
    print_header()
    run_event_loop()


def print_header():
    print('-----------------------------------------------------------------------------------------------------------')
    print(' Welcome to the JOURNAL APP ')
    print('-----------------------------------------------------------------------------------------------------------')


def run_event_loop():
    print('What do you want to do with your journal? ')
    cmd = 'EMPTY'
    journal_name = 'default'
    journal_data = journal.load(journal_name)  # []  # list()

    while cmd != 'x' and cmd:
        # a string is a collection, thus the 'truthiness' of a string is evaluatable
        # - an empty string evaluates to false
        # - non-empty string evaluates to true
        cmd = input('[L]ist entries, [A]dd an entry, E[x]it: ')
        cmd = cmd.lower().strip()

        if cmd == 'l':
            list_entries(journal_data)
        elif cmd == 'a':
            add_entries(journal_data)
        elif cmd != 'x' and cmd:
            print("Sorry, we don't understand '{}'.".format(cmd))

    print('Done, goodbye.')
    journal.save(journal_name, journal_data)


def list_entries(data):
    print('Your journal entries:')
    entries = reversed(data)
    # idx is the index part of the tuple created by enumerate
    # entry is the data part of the tuple read from the entries list
    for idx, entry in enumerate(entries):
        print('* [{}] {}'.format(idx+1, entry))


def add_entries(data):
    text = input('Type your entry, <enter> to exit: ')
    journal.add_entry(text, data)
    # avoid directly working with data structures if possible
    # data.append(text)

# check to see if we are being called directly as our own script
# or if we have been imported as a module
# when this is executed directly, it will known itself as "__main__"
# when this is imported as a module, it will knowi itself as "program" (the filename)
if __name__ == '__main__':
    main()
