from datetime import datetime

raw_date = "01-May-12"
date_format = "%d-%B-%y"

parsed_date = datetime.strptime(raw_date, date_format)
date_str = parsed_date.strftime("%m/%d/%y")
print(date_str)