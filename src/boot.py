import network
import time
import config


def do_connect():
    wifi_ssid = config.WIFI_SSID
    wifi_password = config.WIFI_PASSWD

    # Wireless config : Station mode
    station = network.WLAN(network.STA_IF)
    station.active(True)

    # Continually try to connect to WiFi access point
    while not station.isconnected():

        # Try to connect to WiFi access point
        print("Connecting...")
        station.connect(wifi_ssid, wifi_password)
        time.sleep(10)

    # Display connection details
    print("Connected!")
    print("My IP Address:", station.ifconfig()[0])


if __name__ == "__main__":
    do_connect()
