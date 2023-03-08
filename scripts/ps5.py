# Made by Caitlyn
# Modified by Lex to work well with a ps5 controller

import argparse
import pygame
import math

import nao


class PS4Controller(object):
    def __init__(self, robot):
        """
        TODO:
        """
        self.robot = robot
        pygame.init()
        pygame.joystick.init()
        self.controller = pygame.joystick.Joystick(0)
        self.controller.init()

        # Last known x and y values
        self.x = 0
        self.y = 0
        self.theta_x = 0
        self.theta_y = 0

    def listen(self):
        """

        :return:
        """
        while True:
            for event in pygame.event.get():
                self.act(event)

    def act(self, event):
        if event.type == pygame.JOYAXISMOTION:
            # Handle joysticks
            axis = event.dict['axis']
            if axis == 0:
                self.x = event.dict['value']
            elif axis == 1:
                self.y = event.dict['value']
            elif axis == 3:
                self.theta_x = event.dict['value']
            elif axis == 4:
                self.theta_y = event.dict['value']

            theta = 0
            if self.theta_x != 0 or self.theta_y != 0:
                theta = math.atan2(-self.theta_x, -self.theta_y)

            if abs(self.x) >= 0.2 or abs(self.y) >= 0.2 or abs(theta) >= 0.1:
                print("\nmoving\n")
                self.robot.walk(self.x, self.y, theta)
            else:
                print("\nwaiting for input\n")
                self.robot.motion_proxy.stopMove()

        elif event.type == pygame.JOYBALLMOTION:
            # Handle joy ball motion
            pass

        elif event.type == pygame.JOYBUTTONDOWN:
            # Handle button presses
            button = event.dict['button']
            if button == 0:  # Cross
                pass
                # self.robot.wave()
            elif button == 1:  # Circle
                self.robot.kick()
            elif button == 2:  # Triangle
                pass
                # self.robot.elephant()
            elif button == 3:  # Square
                pass
                # self.robot.saxophone()
            elif button == 4:  # L1
                if not self.robot.sit:
                    self.robot.stop_walking()
                else:
                    self.robot.posture_proxy.goToPosture("StandInit", 0.8)
                    self.robot.sit = False
            elif button == 5:  # R1
                pass
                # self.robot.macarena()
            elif button == 6:  # L2
                pass
            elif button == 7:  # R2
                pass
            elif button == 8:  # Share
                pass
                # self.robot.take_picture()
            elif button == 9:  # Options
                self.robot
            elif button == 10:  # PS4
                print("\033[91m Shutting down \033[0m")
                self.robot.rest()
                self.robot.sit = True
                pygame.joystick.quit()
                exit()
            elif button == 11:  # Left joystick
                pass
            elif button == 12:  # Right joystick
                pass
        elif event.type == pygame.JOYBUTTONUP:
            # Handle button up
            pass
        elif event.type == pygame.JOYHATMOTION:
            # Handle joy hat motion (arrow keys)
            print("joy hat")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Control NAO with a PS4 controller")
    parser.add_argument(
        "-ip", type=str, help="IP address of the robot", default="nao.local")
    parser.add_argument("-port", type=int,
                        help="Port of the robot", default=9559)

    args = parser.parse_args()
    ps4 = PS4Controller(nao.NAO(args.ip, args.port))
    ps4.listen()
