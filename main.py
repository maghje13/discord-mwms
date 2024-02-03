from discord_webhook import DiscordWebhook
import sys


# message function
def send_message(webhook, message):
    hook = DiscordWebhook(url=str(webhook), content=str(message))
    response = hook.execute()

try:
    if sys.argv[1]:
        webhooks = open(sys.argv[1], "r")
        input_message = str(input("Message:\n"))
        for line in webhooks:
            send_message(line.strip(), input_message)
except IndexError:
    print("Invalid arguments!\nCorrect usage: python main.py <webhooks file path>")
