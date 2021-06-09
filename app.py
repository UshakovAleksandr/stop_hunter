from api import app, api
from config import Config
from api.resources.client import ClientResourceList, ClientResource, ClientResponseResource

api.add_resource(ClientResourceList, "/client")
api.add_resource(ClientResource, "/client/<int:client_id>")
api.add_resource(ClientResponseResource, "/stop_hunter/client/request")

if __name__ == '__main__':
    app.run(debug=Config.DEBUG, host="0.0.0.0")
