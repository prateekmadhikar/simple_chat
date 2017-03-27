import json


def serialize(obj):
    return json.dumps(obj).encode('utf-8')


class User:

    def __init__(self, id, socket):
        self.id = id
        self.socket = socket

    def __eq__(self, other):
        return self.id == other.id

    @property
    def is_alive(self):
        return self.socket.closed is False


    def send_message(self, group, from_user, message):
        message = {
            'type': 'message',
            'group_id': group.id,
            'from': from_user.id,
            'message': message
        }

        self.socket.send(serialize(message))
