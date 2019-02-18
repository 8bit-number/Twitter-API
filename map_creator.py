from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
import folium
from parse_tw import get_users, number_of_friends, user_name


geolocator = Nominatim(user_agent="specify_your_app_name_here")
geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)


def map(path, name):
    """
    creates an html-map
    :param d:
    :return:
    """

    d = {}
    for each in path:
        if each["location"] and each["name"] and each["friends_count"] and each["followers_count"]:
            loc = geolocator.geocode(each["location"], timeout=10)
            # print(loc.latitude, loc.longitude)
            if loc:
                d[each["name"]] = [each["followers_count"], each["friends_count"], each["location"], list(loc)]
    coordes = dict()
    for person in d:
        coordes[person] = [d[person][3][1], d[person][3][0]]

    map = folium.Map(zoom_start=21)
    freq = {}
    for coor in coordes:
        counter = [i[1] for i in list(coordes.values())].count(coordes[coor][1])
        if coordes[coor][1] not in freq:
            freq[coordes[coor][1]] = [coor]
        else:
            freq[coordes[coor][1]] = [coor] + freq[coordes[coor][1]]


    for each in freq:
        loc = geolocator.geocode(each, timeout=10)
        if loc:
            folium.Marker([loc.latitude,
                           loc.longitude],
                          popup='{} are here'.format(", ".join(freq[each])),
                          icon=folium.Icon(color='yellow')).add_to(map)
    fn = "/home/nastya/PycharmProjects/lab3/templates/{}.html".format(name)
    map.save(fn)
    print("saved as {}.html in you computer".format(name))
    return fn

if __name__ == "__main__":
    name = user_name()
    lim = 100
    loc = get_users(name, lim)
    map(loc, name)
