#!/usr/bin/env python
# coding: utf-8
import smbus
import time
import math
class ControlCar(object):
    #We 
    def get_i2c_device(self, address, i2c_bus):
        self._addr = address
        if i2c_bus is None:
            return smbus.SMBus(1)
        else:
            return smbus.SMBus(i2c_bus)

    def __init__(self):
        # Create I2C device.
        self._device = self.get_i2c_device(0x16, 1)

    def write_u8(self, register, data):
        try:
            self._device.write_byte_data(self._addr, register, data)
        except:
            print('Error occured!')
    def write_reg(self, register):
        try:
            self._device.write_byte(self._addr, register)
        except:
            print('Error occured while writing to register!')

    def write_array(self, register, data):
        try:
            # self._device.write_block_data(self._addr, reg, data)
            self._device.write_i2c_block_data(self._addr, register, data)
        except:
            print('Error occured while writing to address!')

    def Ctrl_Car(self, l_dir, leftSpeed, r_dir, rightSpeed):
        try:
            register = 0x01
            data = [l_dir, leftSpeed, r_dir, rightSpeed]
            self.write_array(register, data)
        except:
            print('Error occured while controlling the car!')
            
    def Control_Car(self, leftSpeed, rightSpeed):
        try:
            if leftSpeed < 0:
                dir1 = 0
            else:
                dir1 = 1
            if rightSpeed < 0:
                dir2 = 0
            else:
                dir2 = 1 
            
            self.Ctrl_Car(dir1, int(math.fabs(leftSpeed)), dir2, int(math.fabs(rightSpeed)))
        except:
            print('Error occured while controlling the car!')

#Left direction 1, right direction 1
    def Car_Run(self, leftSpeed, rightSpeed):
        try:
            self.Ctrl_Car(1, leftSpeed, 1, rightSpeed)
        except:
            print('Error occured while driving straight!')

    def Car_Stop(self):
        try:
            register = 0x02
            self.write_u8(register, 0x00)
        except:
            print('Error occured while trying to stop!')
#Left direction 0, right direction 0
    def Car_Back(self, leftSpeed, rightSpeed):
        try:
            self.Ctrl_Car(0, leftSpeed, 0, rightSpeed)
        except:
            print('Error occured while driving backwards!')

            #Left direction 0, right direction 1
    def Car_Left(self, leftSpeed, rightSpeed):
        try:
            self.Ctrl_Car(0, leftSpeed, 1, rightSpeed)
        except:
            print  ('Error occured while turning to the left!')
#Left direction 1, right direction 0
    def Car_Right(self, leftSpeed, rightSpeed):
        try:
            self.Ctrl_Car(1, leftSpeed, 0, rightSpeed)
        except:
            print('Error occured while turning to the right!')
#Left direction 0, right direction 1
    def Car_Spin_Left(self, leftSpeed, rightSpeed):
        try:
            self.Ctrl_Car(0, leftSpeed, 1, rightSpeed)
        except:
            print('Error occured while turning to the left!')
#Left direction 1, right direction 0
    def Car_Spin_Right(self, leftSpeed, rightSpeed):
        try:
            self.Ctrl_Car(1, leftSpeed, 0, rightSpeed)
        except:
            print('Error occured while turning to the right!')

    def Ctrl_Servo(self, id, turningAngle):
        try:
            data = [id, turningAngle]
            register = 0x03
            if turningAngle < 0:
                turningAngle = 0
            elif turningAngle > 180:
                turningAngle = 180
            self.write_array(register, data)
        except:
            print('Error occured while controlling the servo!') 
