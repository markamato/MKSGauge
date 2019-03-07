import time
import serial


class MKSGauge:

	defaultNodeID = '@253'
	terminator = ';FF'
	defaultBaud = 9600;
	defaultTimeout = .1;
	defaultPortID = '/dev/ttyUSB0'
	
	# Defines, go do defines here
	pressure = 'PR4'
	setpoint1Status = 'SS1'
	setpoint1Hysteresis = 'SH1'
	setpoint1Enable = 'EN1'
	setpoint1Direction = 'SPD1'
	setpoint2Status = 'SS2'
	setpoint2Hysteresis = 'SH2'
	setpoint2Enable = 'EN2'
	setpoint2Direction = 'SPD2'
	setpoint3Status = 'SS3'
	setpoint3Hysteresis = 'SH3'
	setpoint3Enable = 'EN3'
	setpoint3Direction = 'SPD3'
	
	
	# Init object
	def __init__(self):
		print 'init!'
	
		
	
	# Open serial object #TODO: speed up port
	def StartSerial(self,serialPort=defaultPortID,baud=defaultBaud,timeout=defaultTimeout):
		self.gaugeSerial = serial.Serial()
		self.gaugeSerial.timeout=timeout
		self.gaugeSerial.baud=baud
		self.gaugeSerial.port=serialPort
		self.gaugeSerial.open()
		#print self.gaugeSerial.name
		return self.gaugeSerial
	
	# Close serial object #TODO: do i need to send an explicit carriage return with this library or is it done for me?
	def StopSerial(self):
		self.gaugeSerial.close()

	
	# set command
	def Set(self,command,value=""):
	    commandstring = self.defaultNodeID+command+'!'+value+self.terminator
	    self.gaugeSerial.write(commandstring) 
	    return self.gaugeSerial.readline()
	    
	# get command
	def Get(self,command):
		commandstring=self.defaultNodeID+command+'?'+self.terminator
		#print commandstring
		self.gaugeSerial.write(commandstring)
		return self.gaugeSerial.readline()
 
	#get pressure
	def GetPressure(self,pres = pressure):
		pressurestring = self.Get(pres)
		return float(pressurestring[7:12])*10**int(pressurestring[13:15])

	    
	
