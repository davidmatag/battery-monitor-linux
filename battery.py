from notification import *

_notify_level = 10

# charge_state may be 'Charging' or 'Discharging'
_charge_state = None
# battery_level is the current battery percentage
_battery_level = None


def _update_values():
    global _charge_state
    global _battery_level

    _charge_state = open("/sys/class/power_supply/BAT1/status", "r").readline().strip()
    _battery_level = int(open("/sys/class/power_supply/BAT1/capacity", "r").readline().strip())


def check_status():
    _update_values()
    # Notify if battery level is low and the battery is not in charging
    if _battery_level <= _notify_level and _charge_state is not "Charging":
        show_notification()


def get_sleep_time():
    # If current battery percentage is closer of the notify level then sleep time is lower
    if _battery_level <= _notify_level + 10:
        return 60
    else:
        return 300
