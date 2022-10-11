# NAO PS5 Control
Control the Nao robot with a ps5 (or ps4) controller.

## Requirements
- python 2
- [pygame](https://www.pygame.org/news)
- [Pillow](https://pypi.org/project/Pillow/)
- [NaoQi](http://doc.aldebaran.com/2-4/dev/python/install_guide.html)

`pygame` and `Pillow` can be installed using pip or the requirements file:

`pip install -r requirements.txt`

`NaoQi` cannot be installed using pip and should be installed following [this link](http://doc.aldebaran.com/2-4/dev/python/install_guide.html).

## Setup
Copy sound files to the robot:

`scp -r sounds/ nao@<robot_ip>:~/`

Connect the robot and the ps5 controller to your laptop.

To connect the ps5 controller via bluetooth follow [this link](http://ros-developer.com/2017/12/14/ps4-controller-bluetooth-ubuntu/).

## Run
`cd scripts/`
`python ps5.py -ip <robot_ip>`

## Controls
| PS4 control    | Action |
|---             |--- |
| Left joystick  | move in x/y direction |
| Right joystick | turn |
| X              | wave |
| O              | kick |
| △              | elephant |
| □              | saxophone |
| ps             | shutdown (robot will go to rest position and disconnect) |
| l1             | Sit down |
| r1             | Macarena |

## Add new motions
- Create a new python file in `motions/`.
- Add the motion to the NAO class.
- Add the motion to a specific button in the PS4 class.
