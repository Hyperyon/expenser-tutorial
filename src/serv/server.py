#!/usr/bin/env python3
import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from datetime import datetime

def red(filename):
    with open(filename, 'r',encoding='utf-8') as f:return f.read()
def ouate(data, filename):
    with open(filename,'w+') as f:f.write(data)
def get_time():
    return datetime.now().strftime('%d/%m %H:%M')

class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Content-type', 'text/html')
        self.end_headers()
    def do_HEAD(self):
        self._set_headers()

    def do_GET(self):
        self._set_headers()
        try:content= open(self.path[1:]).read()
        except:content=open("data.json").read()
        self.end_headers()
        self.wfile.write(bytes(content, "UTF-8"))

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode("utf-8")
        self._set_headers() #print information
        self.end_headers()
        req = json.loads(post_data)
        
        if self.path == '/lapost':
            old_data = json.loads(red("data.json"))
            next_id = max([x['id'] for x in old_data])+1
            req = {"id":next_id,**req['expenses']}
            data = [req] + old_data
            ouate(json.dumps(data,indent=4),"data.json")

        elif self.path == '/edit_piaf':
            data = json.loads(red("data.json"))
            print(req['expenses']['id'],'-----')
            for index, item in enumerate(data):
                if item['id'] == req['expenses']['id']:
                    data[index] = {**req['expenses']}
                    print(data[index])
                    break
            ouate(json.dumps(data,indent=4),"data.json")

        else:
            data = [{'reply':False}]

        self.wfile.write(bytes(json.dumps(data),"UTF-8"))

def run(server_class=HTTPServer, handler_class=S, port=80):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print('Starting httpd...')
    httpd.serve_forever()

if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()