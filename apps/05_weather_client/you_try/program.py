from pip._vendor import requests
import bs4
import collections

# import collections to use named tuples -
# a named tuple is a data collection with named indexes
WeatherReport = collections.namedtuple('WeatherReport',
                                       'location, condition, high, low')


def main():
    # print the header
    print_the_header()
    # get the location of the user

    # why does this work if there is a space after the question mark, but not work if there is no space?
    user_zip = input('What zipcode do you want the weather for (e.g. 90210)? ')
    html = get_html_from_web(user_zip)
    # parse the html
    forecast = get_weather_from_html(html)
    # display the forecast
    print('In {} ({}) the weather is {} with a high of {} and a low of {}.'.format(
        forecast.location,
        user_zip,
        forecast.condition,
        forecast.high,
        forecast.low))


def get_weather_from_html(html):
    # CSS references to get the data points we want
    # City Name: inner-content > div.city-header > div > div > city-header > div > h1
    # Current Weather: div.condition-icon.small-6.medium-12.columns > p
    # High Temp: div.hi-lo > span.hi
    # Low Temp:  div.hi-lo > span.lo

    # pass beautiful soup the complete html retrieved from the web
    soup = bs4.BeautifulSoup(html, 'html.parser')
    # use css references within beautiful soup to find the data we are looking for within the page
    cityname = soup.find("div", class_="columns small-12").find('h1').get_text(strip=True)
    condition = soup.find("div", class_="condition-icon small-6 medium-12 columns").find('p').get_text(strip=True)
    condition = condition.lower()
    upper_temp = soup.find("div", class_="hi-lo").find("span", class_="hi").get_text(strip=True)
    lower_temp = soup.find("div", class_="hi-lo").find("span", class_="lo").get_text(strip=True)

    # assign our values to each of the named index locations in the named tuple
    report = WeatherReport(location=cityname, condition=condition, high=upper_temp, low=lower_temp)
    return report


def print_the_header():
    print('------------------')
    print(' Weather App')
    print('------------------')
    print()


def get_html_from_web(user_zip):
    url = 'http://www.wunderground.com/weather-forecast/{}'.format(user_zip)
    response = requests.get(url)
    # this will print the first 250 characters of the response
    # alternatives syntax: [:250]
    # can specify any arbitrary delineation point e.g. [250:500] etc
    # print(responst.text[0:250]); this construct is called "slicing"
    return response.text


if __name__ == '__main__':
    main()
