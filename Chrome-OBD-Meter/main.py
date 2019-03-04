import eel
import obd

#obd.logger.setLevel(obd.logging.DEBUG)
connection = obd.OBD()

@eel.expose
def python_function2():
    response_s = connection.query(obd.commands.SPEED)
    response_r = connection.query(obd.commands.RPM)
    speed = response_s.value.magnitude
    rpm = response_r.value.magnitude
    ind_values = {'speed': speed, 'rpm': rpm}
    return ind_values

web_app_options = {
    "mode": "chrome-app",
    "port": 8080,
    "chromeFlags": [
            "--start-fullscreen",
    ]
}

eel.init("web")
eel.start("main.html", options=web_app_options)
