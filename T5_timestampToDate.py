from datetime import date

class DateObject:
  def __init__(self, year, month, day, week):
    self.year = year
    self.month = month
    self.day = day
    self.week = week
  def __str__(self):
    return "Year: {}, Month: {}, Day: {}, Weak: {}".format(self.year, self.month, self.day, self.week)

#Get date object with week number
def getDateObject(timestamp):
  d = date.fromtimestamp(timestamp)

  year = d.year
  month = d.month
  day = d.day
  week = d.isocalendar()[1]

  return DateObject(year, month, day, week)

# Test code
print("Timestamp =",1615222448)
print(str(getDateObject(1615222448)))
