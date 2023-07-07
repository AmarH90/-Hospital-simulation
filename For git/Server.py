from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs
student_dict = {"0":["Alfa0","Omega0","24","AB poz","Sputnik V","Spol"],}
class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.log_message("Incoming GET request...")
        try:
            id_korisnika = parse_qs(self.path[2:])["id_korisnika"][0]
        except:
            self.send_response_to_client(404, "Incorrect parameters provided")
            self.log_message("Incorrect parameters provided")
            return
        if id_korisnika in student_dict.keys():
            self.send_response_to_client(200, student_dict[id_korisnika])
        else:
            self.send_response_to_client(400, "Id not found")
            self.log_message("Id not found")
    def do_POST(self):
        self.log_message("Incoming POST request...")
        data = parse_qs(self.path[2:])
        try:
            student_dict[data["id_korisnika"][0]] = [data["name"][0], data["last_name"][0], data["years"][0], data["blod_type"][0], data["vakcine_send"][0], data["sex_of_user"][0]]
            self.send_response_to_client(200,student_dict)
        except KeyError:
            self.send_response_to_client(404,"Incorrect parameters provided")
            self.log_message("Incorrect parameters provided")
    def send_response_to_client(self, status_code, data):
        self.send_response(status_code)
        self.send_header("Content-type", "text/plain")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(str(data).encode())
server_address = ("127.0.0.1", 8080)
http_server = HTTPServer(server_address, RequestHandler)
http_server.serve_forever()