import datetime

def datetime_filename():
    now = datetime.datetime.now()
    formatted_date = now.strftime("%Y-%m-%d")
    formatted_time = now.strftime("%H-%M-%S")
    filename = f"{formatted_date}_{formatted_time}"
    return filename
