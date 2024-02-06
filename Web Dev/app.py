from time import time

name = 'AIT Chat'
users = [] # names
messages = {} # key = sender, value = [{receiver, time, message }]



def send(sender, receiver, msg):
    if sender not in users:
        users.append(sender)
    if receiver not in users:
        users.append(receiver)


    if sender not in messages:
        messages[sender] = []
    
    messages[sender].append({"receiver": receiver, "time": time(), "message": msg})

    print()
    print(messages)
    print()

def get_from_single_user(sender, receiver):
    if sender not in messages:
        return []
    
    output = []

    for d in messages[sender]:
        if d["receiver"] == receiver:
            output.append(d)

    return output

### Web Dev Lab
### 1. show all messages sent by sender
### 2. show all messages in database
### 3. show all messages received by receiver


if __name__ == "__main__":

    while True:
        instruction = input('instruction: ')
        if instruction == 'send':
            sender = input('Sender: ')
            receiver = input('Receiver: ')
            message = input('Message: ')
            send(sender, receiver, message)
        elif instruction == 'get_single':
            sender = input('sender: ')
            receiver = input('receiver: ')
            print(f'messages sent by {sender} to {receiver} are : ', get_from_single_user(sender, receiver))
