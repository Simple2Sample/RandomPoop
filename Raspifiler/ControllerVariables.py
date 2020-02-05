
#Range for joysticks are 16 bits or 65536 values. 32768 is center position.
#Be aware of deadzones!!!
#Code00
#xAxis1
code = [0]*(500)
code[0]= 32768


#Code01
#yAxis1
code[1]= 32768

#Code02
#xAxis2.

code[2]=32768

#Code03
#xAxis2
code[3]= 32768
#Code04
#Something about the 4 buttons on the side. Value changes by which button is pressed
code[4]=0

#yAxis2
code[5]=32768
#Code05
#10 bit trigger. Ranging from 0 to 1023. 0 is unpressed
#rightTrigger
code[9]=0

#LeftTrigger
code[10]=0

#Code304
#AButton
code[304]=0


#Code305
#BButton
code[305]=0


#Code306
#XButton
code[306]=0


#Code307
#YButton
code[307]=0

#Select Button
code[310]=0
#Start Button
code[311]=0


#Code16
#Value ranges from -1 to 1. -1 means Left and 1 means right. 0 is no input
#XCross
code[16]=0

#Code17
#Value ranges from -1 to 1. -1 means up and 1 means down.
#YCross
code[17]=0
