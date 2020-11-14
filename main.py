from ApiClient import api_client
from AnalyzeManager import analyze_change
from MailManager import mail_manager
import time

if __name__ == "__main__":
    current_value = 0
    last_value = 0

    while True:
        current_value = api_client.get_value()

        if last_value == 0:
            last_value = current_value
        else:
            print("Current Value: " + str(current_value))
            print("Last Value : " + str(last_value))
            analyzedValue = analyze_change.analyze(current_value, last_value, 0.10)
            print("Change Percent: " + str(analyzedValue["percent"]))

            if analyzedValue["send"]:
                mail_manager.send_mail(current_value, analyzedValue["percent"])
                last_value = current_value
                send = False

        time.sleep(30)
