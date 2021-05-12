from naoqi import ALProxy

motion = ALProxy("ALMotion", "192.168.0.48", 9559)


motion.moveInit()
motion.moveTo(0.5, 0, 0)
