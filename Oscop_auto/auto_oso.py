import pyvisa
from time import sleep
## for printing into .csv file
import os

filepath = './data.csv'
#To get instrument IDs from python interface
#   1.  import pyvisa  (pip install pyvisa-py)
#   2.  rm = pyvisa.ResourceManager()
#   3. print(rm.list_resources()) (copy output of this line, paste into script)


rm = pyvisa.ResourceManager()
supply = rm.open_resource('USB0::0x1AB1::0x0E11::DP8C222401950::INSTR') #DP denotes pwr supply
dmm = rm.open_resource('USB0::0x1AB1::0x09C4::DM3R222300640::INSTR') #DM = multimeter

dmm.write(':FUNCtion:VOLTage:DC')  #set multimeter to DC voltage

#set pwr supply to 5v, 200mA
supply.write(':OUTP CH1,OFF') #ensure PS is off
supply.write(':APPL CH1,0,0.2') #0v, 0.2A to begin

supply.write(':OUTP CH1,ON')
for v in range(5, 10, 1):
    supply.write(':APPL CH1,' + str(v) + ',0.2')
    sleep(2)
    vMeasure = float( dmm.query(':MEASure:VOLTAGE:DC?') )
    
    print("{}  {}".format(v, vMeasure))  #print PS output vs. MM measurement

    with open(filepath, 'a') as file:
        if os.stat(filepath).st_size == 0:
            ## make table, char width 12.2f and 13.2f, f for floating pt
            file.write("Setpoint [V], Measured [V]\n")
        file.write("{:12.2f}, {:13.2f}\n".format(v, vMeasure)) 
    file.close()



supply.write(':OUTP CH1,OFF')  #turns supply off
supply.write(':APPL CH1,0,0')  #zeros outputs
