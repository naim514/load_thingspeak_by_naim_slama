l = ""

def on_button_pressed_a():
    WiFiIoT.send_generic_http(WiFiIoT.httpMethod.GET, "api1", "")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_http_recevid(HTTP_Status_Code, Data):
    global l
    l = WiFiIoT.get_value("feeds", Data)
    basic.show_string(WiFiIoT.get_value("field1", l[0]))
WiFiIoT.on_HTTP_recevid(on_http_recevid)
