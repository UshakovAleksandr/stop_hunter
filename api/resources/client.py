from api.models.client import ClientModel
from api import Resource, abort, app
from flask import request


class ClientResponseResource(Resource):

    @app.validate("client_request", "request")
    def get(self):
        try:
            email = request.json["email"]
            client = ClientModel.query.filter_by(email=email).first()
            if not client:
                return f"Client not found in 'stop_hunter' service", 404
        except Exception as e:
            return {"message": str(e)}, 400
        return client.to_dict(), 200


class ClientResource(Resource):

    def get(self, client_id):
        try:
            client = ClientModel.query.get(client_id)
            if not client:
                return f"No client with id={client_id}", 404
        except Exception as e:
            return {"message": str(e)}, 400
        return client.to_dict(), 200

    def delete(self, client_id):
        try:
            client = ClientModel.query.get(client_id)
            if not client:
                return f"No client with id={client_id}", 404
            client.delete()
        except Exception as e:
            return {"message": str(e)}, 400
        return f"User with id={client_id} deleted", 200


class ClientResourceList(Resource):

    def get(self):
        try:
            clients = ClientModel.query.all()
            if not clients:
                return f"No clients yet", 404
        except Exception as e:
            return {"message": str(e)}, 400
        return [client.to_dict() for client in clients], 200

    @app.validate("client", "client")
    def post(self):
        try:
            client = ClientModel(**request.json)
            client.save()
        except Exception as e:
            return {"message": str(e)}, 400
        return client.to_dict(), 201
