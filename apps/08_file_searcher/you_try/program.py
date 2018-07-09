import os
import collections

SearchResult = collections.namedtuple('SearchResult',
                                      'file, line, text')

# array.append() vs array.extend()
# .append adds an object at the end of the array. This can be any object including another array.
# e.g. [1, 2, 3].append([4, 5]) yields [1, 2, 3, [4, 5]]
# .extend adds objects to the end of the array. This can be any object including another array.
# e.g. [1, 2, 3].extend([4, 5]) yields [1, 2, 3, 4, 5]

# current problem: search results only appearing from the last text file searched, not all text files
def main():
    print_header()
    folder = get_folder_from_user()
    if not folder:
        print("Sorry, we can't search that location")

    text = get_search_text_from_user()
    if not text:
        print("Sorry, we can't search for nothing")

    matches = search_folder(folder, text)

    for m in matches:
        # print(m)
        print('-------- MATCH --------')
        print('file: ' + m.file)
        print('line: ' + str(m.line))
        print('match: ' + m.text.strip())
        print()


def print_header():
    print('---------------------')
    print('File search programme')
    print('---------------------')


def get_folder_from_user():
    folder = input('What folder would you like to search? ')
    if not folder or not folder.strip():
        return None

    if not os.path.isdir(folder):
        return None

    return os.path.abspath(folder)


def get_search_text_from_user():
    text = input("What are you searching for (single word only)? ")
    return text.lower()


def search_folder(folder, text):
    all_matches = []
    items = os.listdir(folder)

    for item in items:
        full_item = os.path.join(folder, item)
        if os.path.isdir(full_item):
            # R E C U R S I O N
            matches = search_folder(full_item, text)
            all_matches.extend(matches)
        else:
            matches = search_file(full_item, text)
            all_matches.extend(matches)
    return all_matches


def search_file(filename, text):
    matches = []
    with open(filename, 'r', encoding='utf-8') as fin:
        line_num = 0
        short_filename = filename.split('\\')
        short_filename = short_filename[len(short_filename)-1]
        for line in fin:
            line_num += 1
            # .find is case sensitive!
            if line.lower().find(text) >= 0:
                m = SearchResult(line=line_num, file=short_filename, text=line)
                matches.append(m)
    return matches

if __name__ == '__main__':
    main()