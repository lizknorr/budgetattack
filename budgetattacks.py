from twilio.rest import TwilioRestClient
import config


def sms(stuffing):

    twilioCli = TwilioRestClient(config.accountSID, config.authToken)
    message = twilioCli.messages.create(body=stuffing, from_=config.myTwilioNumber, to=config.myCellPhone)
