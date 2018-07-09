import os
import platform
import subprocess
import cat_service


def main():
    # print the header
    print_header()
    # get or create output folder
    folder = get_or_create_output_folder()
    print('Found or created folder: ' + folder)
    # download cats
    download_cats(folder)
    # display cats
    display_cats(folder)


def print_header():
    print('-------------')
    print('CAT FACTORY')
    print('-------------')


def get_or_create_output_folder():
    # __file__ represents the current full file location of the program
    # so we get the directory from the full path of the file to save files locally with the program
    base_folder = os.path.dirname(__file__)
    folder = 'cat_pictures'
    full_path = os.path.abspath(os.path.join(base_folder, folder))

    # check to see if the folder we want to create already exists, and if not, create it
    if not os.path.exists(full_path) or not os.path.isdir(full_path):
        print("Creating new directory at {}".format(full_path))
        os.mkdir(full_path)

    return full_path


def download_cats(folder):
    cat_count = 8
    print("Contacting server to download cats...")
    # a standard for loop iterating through a range of integers
    for i in range(1, cat_count+1):
        name = 'lolcat_{}'.format(i)
        print('Downloading cat {}'.format(i))
        cat_service.get_cat(folder, name)
    print("Done!")


def display_cats(folder):
    # open folder using the correct subprocess call for three operating systems
    print("Displaying cats in file browser...")
    if platform.system() == 'Darwin':
        subprocess.call(['open', folder])
    elif platform.system() == 'Windows':
        subprocess.call(['explorer', folder])
    elif platform.system() == 'Linux':
        subprocess.call(['xdg-open', folder])
    else:
        print("Sorry, I don't know your operating system.")


if __name__ == '__main__':
        main()
