def analyze(current_value, last_value, percent):
    try:
        change_percent = ((last_value - current_value) / current_value) * 100
        if change_percent >= percent or change_percent <= -percent:
            return True, change_percent
        else:
            return False
    except Exception as ex:
        print(ex)
