let l = ""
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    WiFiIoT.sendGenericHttp(WiFiIoT.httpMethod.GET, "api1", "")
})
WiFiIoT.on_HTTP_recevid(function on_http_recevid(HTTP_Status_Code: string, Data: string) {
    
    l = WiFiIoT.get_value("feeds", Data)
    basic.showString(WiFiIoT.get_value("field1", l[0]))
})
