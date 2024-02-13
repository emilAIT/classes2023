from time import time
from flask import Flask, request

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
def get_messages_by_sender(sender):
    return messages.get(sender, [])

### 2. show all messages in database
def get_all_messages():
    return messages

### 3. show all messages received by receiver
def get_messages_by_receiver(receiver):
    output = []
    for sender, lst in messages.items():
        for d in lst:
            if d['receiver'] == receiver:
                output.append(d)
    return output


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


## /COST
            

@app.route('/cost')
def cost():
    d = request.args.to_dict()
    max_name = None
    max_value = 0
    total_cost = 0
    for key, value in d.items():
        val = int(value)
        if max_value < val:
            max_name = key
            max_value = val
        total_cost += val

    return f'Samiy dorogoy napitok {max_name} tsenoy {max_value}, Total cost is {total_cost}, Average cost is {total_cost/len(d)}'
