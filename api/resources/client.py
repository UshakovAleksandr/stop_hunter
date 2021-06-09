from api.models.client import ClientModel
from api import Resource, abort
from flask import request


class ClientResponseResource(Resource):

    def get(self):
        email = request.json["email"]
        client = ClientModel.query.filter_by(email=email).first()
        if not client:
            abort(404, error=f"No client")
        return client.to_dict(), 200


class ClientResource(Resource):

    def get(self, client_id):
        client = ClientModel.query.get(client_id)
        if not client:
            abort(404, error=f"No client with id={client_id}")
        return client.to_dict(), 200

    def delete(self, client_id):
        client = ClientModel.query.get(client_id)
        if not client:
            abort(404, error=f"No client with id={client_id}")
        client.delete()
        return f"User with id={client_id} deleted", 200


class ClientResourceList(Resource):

    def get(self):
        clients = ClientModel.query.all()
        if not clients:
            abort(404, error=f"No clients yet")
        return [client.to_dict() for client in clients], 200

    def post(self):
        client = ClientModel(**request.json)
        try:
            client.save()
            return client.to_dict(), 201
        except:
            abort(404, error=f"An error occurred while adding new client" \
                             "or a client with such email is already exist. " \
                             "You can only add a client with unique email")
