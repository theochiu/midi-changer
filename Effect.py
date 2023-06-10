
class Effect(object):
    
    def __init__(self, name, cc_num, pin_num, pullup=True):
    	self.name = name
    	self.cc_num = cc_num
    	self.pressed = True
    	
    	# encapsulate the footswitch as well
    	self.pin_num = pin_num
    	self.pullup = pullup


