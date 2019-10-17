from crawler import crawl
# import datetime

# start = datetime.datetime.strptime("2000-01-01", "%Y-%m-%d")
# end = datetime.datetime.strptime("2019-10-10", "%Y-%m-%d")
# date_array = \
#     (start + datetime.timedelta(days=x) for x in range(0, (end-start).days))
# dates = []
# for date_object in date_array:
#     dates.append(date_object.strftime("%Y-%m-%d"))
# print(dates)
# if __name__ == '__main__':
#     tags = ['$MSFT']
#     for date in dates:
#         crawl(date, tags)

if __name__ == '__main__':
    dates = ['2019-10-05']
    tags = ['$MSFT']
    for date in dates:
        crawl(date, tags)