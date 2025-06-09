class Mobile:
    camera=True
    touchscreen=True
    maxbattery="100%"
    internet=True
    volumebuttons=2
    powerbuttons=1
    cameras="varies"

    def snap_picture(self,x):
        print(x,"took a phot")
        
    def connect_to_wifi(self, x):
        print(x,"connected to wifi")

iphone16=Mobile()
samsung_galaxy_s25=Mobile()
realme_gT_7t=Mobile()
Nokia3310=Mobile()

print(Nokia3310.connect_to_wifi)
print(realme_gT_7t.volumebuttons)

iphone16.snap_picture("iPhone16")
samsung_galaxy_s25.connect_to_wifi("S25")