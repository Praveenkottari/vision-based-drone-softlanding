from pymavlink import mavutil
import time
import sys
# Connect to the Pixhawk on the specified device and baudrate
master = mavutil.mavlink_connection('/dev/ttyUSB0', baud=115200)

# Wait for the heartbeat to ensure a connection is established
while not master.wait_heartbeat():
    print("Waiting for heartbeat...")
    time.sleep(1)

print("Heartbeat received!")

# while True:
#     msg = master.recv_match(blocking=True)
#     print(msg)
#Set Mode
# master.mav.command_long_send(
#     master.target_system,
#     master.target_component,
#     176,
#     0,
#     192,
#     0,
#     0,
#     0,
#     0,
#     0,
#     0
# )

# Arm the vehicle
# master.arducopter_arm("manual")
# master.mav.command_long_send(
#     master.target_system,
#     master.target_component,
#     mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,
#     0,
#     0,
#     0,
#     0,
#     0,
#     0,
#     0,
#     0
# )
# msg = master.recv_match(type="COMMAND_ACK",  blocking=True)
# print(msg)
# print("Vehicle armed!")

# while not master.motors_armed():
#     print("Arming Motor..")
#     time.sleep(1)


# # Set motor rotation speed (values between 1000 and 2000)
# master.mav.manual_control_send(master.target_system, motor_speed, 0,0,0,0,0)
# Send motor command to the Pixhawk
def rotate_motor(motor):
    master.mav.command_long_send(
        master.target_system,
        master.target_component,
        310,
        0,
        0,
        1,
        0,
        0,
        motor,
        0,
        0
    )
# master.mav.command_long_send(
#     master.target_system,
#     master.target_component,
#     mavutil.mavlink.MAV_CMD_DO_MOTOR_TEST,
#     0,
#     1,
#     1,
#     1500,
#     1,
#     0,
#     0,
#     0
# )


    # msg = master.recv_match(type="COMMAND_ACK",  blocking=True)
    # print(msg)


# rotate_motor(int(sys.argv[1]))
# for i in range(4):
#     rotate_motor(i+1)
#     time.sleep(2)
# # print(f"Motor speed set to {motor_speed}")

# # Disarm the vehicle after 5 seconds (change as needed)
# time.sleep(5)
# master.arducopter_disarm()
# print("Vehicle disarmed!")
# msg = master.recv_match(type="COMMAND_ACK",  blocking=True)
# print(msg)
