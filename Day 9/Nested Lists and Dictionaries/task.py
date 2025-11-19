# capitals={
#     "France": "Paris",
#     "Germany":"Berlin",
# }

#nested list in dictionary
# travel_log={
#     "France": ["Paris", "Lille", "Dijon"],
#     "Germany": ["Stuttgart", "Berlin"],
# }
#See if you can figure out how to print out "Lille" from the nested List called travel_log.
# print(travel_log["France"][1])
#
# nested_list=["A","B",["C","D"]]
# print(nested_list[2][1])

travel_log={
    "France": {
        "city_visited": ["Paris", "Lille", "Dijon"],
        "total_visits":8,
    },
    "Germany": {
        "city_visited":["Stuttgart", "Berlin","Hamburg"],
        "total_visits":5,
    }
}
print(travel_log["Germany"]["city_visited"][0])

