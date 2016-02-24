import requests

calendarFormat = "https://illinois.edu/calendar/list/{}"

validCalendars = []
#I bet you've never seen such a hacky way to scrape calendars
for i in range(0, 5000):
    r = requests.get(calendarFormat.format(i))
    if r.status_code is not 302:
        validCalendars.append(i)
        
print(validCalendars)