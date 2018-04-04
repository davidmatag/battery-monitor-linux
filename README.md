# Battery Monitor
Low battery notifier like Windows, for Linux.

# Critical level

Identify in your computer which is the critical level of the battery(percentage), and in the file "main.py" find this:
`criticalBat = ` "put here the percentage(without %)"

For example if your critical battery level are 20%, so you need to put this: `criticalBat = 20`

Note: The default value is 10%, so if this your critical battery level are 10% you don't need to change anything.


# Configure language of the notification:
In the file "main.py" find this:
`from low_battery_en import *`

For spanish change "`en`" to "`es`"

# Screenshot
<img src="https://image.ibb.co/nGSuf7/battery_monitor.png" />
