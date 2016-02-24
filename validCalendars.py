import requests

calendarFormat = "https://illinois.edu/calendar/list/{}"

validCalendars = []
#I bet you've never seen such a hacky way to scrape calendars
for i in range(0, 10000):
    r = requests.get(calendarFormat.format(i))
    #if all is well with the calendar
    if r.status_code is 200:
        validCalendars.append(i)
        
#print(validCalendars)
with open("validCalendars.txt", "w") as file:
    for validCalendarCode in validCalendars:
        file.write(calendarFormat.format(validCalendarCode))