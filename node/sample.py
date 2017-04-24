#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
import datetime
import re

# Import other libraries
from rospeex_if import ROSpeexInterface
from std_msgs.msg import Int32

class Demo(object):
    """ Demo class """
    def __init__(self):
        """ Initializer """
        self._interface = ROSpeexInterface()
        self.pub = rospy.Publisher("/order_topic",Int32 ,queue_size = 1)
    def sr_response(self, message):
        
        pattern11 = re.compile('Take the').search(message)
        pattern12 = re.compile('take the').search(message)

        pattern21 = re.compile('Stop the').search(message)
        pattern22 = re.compile('stop the').search(message)

        order11 = re.compile('order').search(message)
        order21 = re.compile('challenge').search(message)

        print 'you said : %s' % message
        
#-------スタートストップコーナー---------------------------
        if pattern11 is not None:
           if order11 is not None:
               print "pattern11_order11"
               self.pub.publish(1)

        if pattern12 is not None:
           if order11 is not None:
              print "pattern12_order_order11"
              self.pub.publish(1)

        if pattern21 is not None:
           if order11 is not None:
              print "pattern21_order_order11"
              self.pub.publish(2)
           elif order21 is not None:
              print "pattern21_order_order21"
                self.pub.publish(3)

        if pattern22 is not None:
           if order11 is not None:
              print "pattern22_order_order11"
              self.pub.publish(2)
           elif order21 is not None:
                print "pattern22_order_order21"
                self.pub.publish(3)
#--------------------------------------------------------

#            text = u""
            # rospeex reply
#            print 'rospeex reply : %s' % text
#            self._interface.say(text, 'ja', 'nict')

    def run(self):
        """ run ros node """
        # initialize ros node
        rospy.init_node('ss_sr_demo')

        # initialize rospeex
        self._interface.init()
        self._interface.register_sr_response(self.sr_response)
#        self._interface.set_spi_config(language='ja', engine='nict')
        self._interface.set_spi_config(language='en', engine='nict')
        rospy.spin()

if __name__ == '__main__':
    try:
        node = Demo()
        node.run()
    except rospy.ROSInterruptException:
        pass
