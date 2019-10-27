


adb shell screencap -p /sdcard/screencut.png
adb pull /sdcard/screencut.png .

adb shell 
input swipe 100 1450 100 100 500

input tap 350 450
input swipe 100 1450 100 100 500


input keyevent 4