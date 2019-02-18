from terminaltables import AsciiTable
from parse_tw import get_users, number_of_friends, user_name


def parser(path):
    """
    takes the json object and shows the table of data that is known about a certain user
    :param path:
    :return: (None)
    """
    variants = ["1 - location", "2 - screen_name", "3 - friends_count", "4 - followers_count",
                "5 - lang", "6 - created_at"]
    for i in variants: print(i)
    choice = input("enter comma-separately all choices you data you want to see about user (eg. 1,2,4): ").split(",")

    d_variants = {
        "1": "location",
        "2": "screen_name",
        "3": "friends_count",
        "4": "followers_count",
        "5": "lang",
        "6": "created_at",
    }

    if choice not in d_variants.keys():
        return "you enetered invalid data"

    fin = [["name"]]
    for i in choice:
        fin[0].append(d_variants[i])

    for each in path:
        temp = []

        temp.append(each["name"])
        for i in choice:
            temp.append(each[d_variants[i]])
        fin.append(temp)


    table = AsciiTable(fin)
    print(table.table)


if __name__ == "__main__":
    num = number_of_friends()
    acct = user_name()
    lst = get_users(acct, num)
    parser(lst)

