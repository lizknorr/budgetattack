from twilio.rest import TwilioRestClient
import config
twilioCli = TwilioRestClient(config.accountSID, config.authToken)
message = twilioCli.messages.create(body='Mr. Watson - Come here - I want to see you.', from_=config.myTwilioNumber, to=config.myCellPhone)
