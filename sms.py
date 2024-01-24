from twilio.rest import Client
import os


def sending_sms(text='Wake up Neo...', receiver='+996704542766'):
    try:
        # account_sid = os.getenv('AC3b7cdefef7a0afd4e3e9b3995f0cf37b')
        # auth_token = os.getenv('928ee8d130335ba095404d52f440c773')
        # @2
        account_sid = 'AC224bd456e112eb4dafdcb8dd98e0dd56'
        auth_token = '80b2a1ee81b594b3269cf8413fbfd5dd'

        client = Client(account_sid, auth_token)

        message = client.messages.create(
            body=text,
            from_='+996703474333',
            to='+996704542766'
        )
        return 'The message was successfully sent!'
    except Exception as ex:
        return 'Something was wrong... :(', ex


def main():
    text = input('please enter your message: ')
    print(sending_sms(text=text, receiver='996704542766'))


if __name__ == '__main__':
    main()
# XAL14HJTS8MG9F8UCZGRTLNQ
#2   #B9FVC4W1E5DMCRLGF8URAQQW