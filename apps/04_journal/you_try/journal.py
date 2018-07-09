import os


def load(name):
    """
    This method creates and loads a new journal.

    :param name: This is the base name of the journal to load.
    :return: A new journal data structure populated with the file data loaded from disk.
    """
    data = []
    filename = get_full_pathname(name)

    # check to see if the file exists before attempting to open it
    if os.path.exists(filename):
        with open(filename) as fileinput:
            for entry in fileinput.readlines():
                data.append(entry.rstrip())
    return data


def save(name, journal_data):
    """
    This method saves the journal data to a file on disk.

    :param name: This is the base name of the journal to save.
    :param journal_data: This is the journal data that is to be saved to disk.
    :return: Null
    """
    # use the path building class of os module to build
    # platform-independent file paths
    filename = get_full_pathname(name)
    print("... saving to: {}".format(filename))

    # if we return without closing the file this can cause problems
    # use a context manager to ensure that the resources are cleaned up
    # this will handle exceptions, early return, falling through
    with open(filename, 'w') as fileout:
        for entry in journal_data:
            # think about better ways to save data to file
            # i.e. don't rely on manually correct formatting of input/output
            fileout.write(entry + '\n')


def get_full_pathname(name):
    """
    Use built-in methods to create a platform-independent file path for loading and saving of files.

    :param name: This is the base name of the journal to be worked with.
    :return: The full filename string.
    """
    filename = os.path.abspath(os.path.join('.', 'journals', name + '.jrl'))
    return filename


def add_entry(text, journal_data):
    """
    Add an entry to the journal by appending a string to the list object representing the journal.

    :param text: The string to be appended as a new list item at the end of the list.
    :param journal_data: The list to append the new list item to.
    :return: Null
    """
    journal_data.append(text)
