import psutil
from win10toast import ToastNotifier
from time import sleep
def getPercent():
    battery = psutil.sensors_battery()
    return battery.percent


def getNotif():
    toast = ToastNotifier()
    toast.show_toast("Battery Life","Battery percentage is %d" % getPercent(),duration=120)
sleep_time = 10 * 60 * 60
while(1):
    percent = getPercent()
    if percent <= 20 :
        getNotif()
    sleep(sleep_time)
