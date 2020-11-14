def analyze(current_value, last_value, percent):
    try:
        change_percent = ((last_value - current_value) / current_value) * 100
        if change_percent >= percent or change_percent <= -percent:
            returnValue = {
                "send": True,
                "percent": change_percent
            }
            return returnValue
        else:
            returnValue = {
                "send": False,
                "percent": change_percent
            }
            return returnValue
    except Exception as ex:
        print(ex)
