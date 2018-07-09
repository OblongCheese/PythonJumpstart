from movie_client import MovieClient
import requests.exceptions

def main():
    print_header()
    search_event_loop()


def print_header():
    print('---------------------------------------')
    print('-----------Movie Search App------------')
    print('---------------------------------------')
    print()


def search_event_loop():
    search = 'ONCE_THROUGH_LOOP'

    while search != 'x':
        try:
            search = input('Title search text (x to exit): ')
            if search != 'x':
                client = MovieClient(search)

                results = client.perform_search()
                print('Found {} results.'.format(len(results)))

                for r in results:
                    print('{} -- {}'.format(r.Year, r.Title))

        # always except errors from most specific to least specific order
        # this is to avoid catching yourself excepting any error, with a generic message, before you except
        # a specific error
        except requests.exceptions.ConnectionError as ce:
            print('There was a problem communicating with the server. Connection failed.')
        except ValueError as ve:
            print('Please enter a valid search string.')
        except KeyError as ke:
            print('Your search term returned zero results.')
        except Exception as x:
            print("That didn't work: {}".format(type(x)))

    print('Exiting...')


if __name__ == '__main__':
    main()