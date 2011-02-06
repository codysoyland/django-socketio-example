from django.http import HttpResponse

buffer = []

def socketio(request):
    socketio = request.environ['socketio']
    if socketio.on_connect():
        socketio.send({'buffer': buffer})
        socketio.broadcast({'announcement': socketio.session.session_id + ' connected'})

    while True:
        message = socketio.recv()

        if len(message) == 1:
            message = message[0]
            message = {'message': [socketio.session.session_id, message]}
            buffer.append(message)
            if len(buffer) > 15:
                del buffer[0]
            socketio.broadcast(message)
        else:
            if not socketio.connected():
                socketio.broadcast({'announcement': socketio.session.session_id + ' disconnected'})
                break

    return HttpResponse()
