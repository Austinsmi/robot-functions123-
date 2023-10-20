import board
import digitalio
import pwmio
import time

from adafruit_motor import motor  # inports a small amount of the  adifruit_motor line

right_motor_forward = (
    board.GP14
)  # initilize the varable right_mortor fowards and attaches it to gp 12
right_motor_backward = (
    board.GP15
)  # initilize the varable right_mortor backwards  and attaches it to gp 13

pwm_Ra = pwmio.PWMOut(
    right_motor_forward, frequency=10000
)  # tells the pico tht it is an component it is an output
pwm_Rb = pwmio.PWMOut(
    right_motor_backward, frequency=10000
)  # tells the pico tht it is an component it is an output


left_motor_forward = board.GP12
left_motor_backward = board.GP13

pwm_La = pwmio.PWMOut(left_motor_forward, frequency=10000)
pwm_Lb = pwmio.PWMOut(left_motor_backward, frequency=10000)

Left_Motor = motor.DCMotor(pwm_La, pwm_Lb)  # configurtion line is needed initilizes left motor
Left_Motor_speed = 0  # Initilizes left_motor_forward spped to 0

Right_Motor = motor.DCMotor(pwm_Ra, pwm_Rb)
Right_Motor_speed = 0



    # Left_Motor_speed = -1  # This makes the left wheel move backwards
    # Left_Motor.throttle
    # time.sleep(3)

def forwards():
    Left_Motor_speed = 1  # makes  the left whell move fowards
    Left_Motor.throttle = Left_Motor_speed
    Right_Motor_speed = 1  # makes  the left whell move fowards
    Right_Motor.throttle = Right_Motor_speed
def backwards():
    Left_Motor_speed = -1  # makes  the left whell move fowards
    Left_Motor.throttle = Left_Motor_speed
    Right_Motor_speed = -1  # makes  the left whell move fowards
    Right_Motor.throttle = Right_Motor_speed
def turn_left():
    Left_Motor_speed = 1  # makes  the left whell move fowards
    Left_Motor.throttle = Left_Motor_speed
    Right_Motor_speed = -1 # makes  the left whell move fowards
    Right_Motor.throttle = Right_Motor_speed
def turn_right():
    Right_Motor_speed = -1 # makes  the left whell move fowards
    Right_Motor.throttle = Right_Motor_speed
    Left_Motor_speed = 1  # makes  the left whell move fowards
    Left_Motor.throttle = Left_Motor_speed

def Stop():
    Right_Motor_speed = 0 # makes  the left whell move fowards
    Right_Motor.throttle = Right_Motor_speed
    Left_Motor_speed = 0  # makes  the left whell move fowards
    Left_Motor.throttle = Left_Motor_speed

while True:
    forwards()
    time.sleep(2)
    turn_left()
    time.sleep(1)
    forwards()
    time.sleep(2)
    turn_left()
    time.sleep(1)
    forwards()
    time.sleep(1)
    turn_right()






    #time.sleep(3)
    #Right_Motor_speed = 1  # makes  the left whell move fowards
    #Right_Motor.throttle = Right_Motor_speed
    #time.sleep(2)
    #Left_Motor_speed = -1  # makes  the left whell move fowards

    #Left_Motor.throttle = Left_Motor_speed# Write your code here :-)
