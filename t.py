from cowin_api import CoWinAPI

pin_code = "400080"
date = '03-05-2021'  # Optional. Default value is today's date
min_age_limit = 18  # Optional. By default returns centers without filtering by min_age_limit 

cowin = CoWinAPI()
available_centers = cowin.get_availability_by_pincode(pin_code, date, min_age_limit)
print(available_centers)