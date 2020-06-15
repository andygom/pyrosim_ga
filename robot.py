import pyrosim
import math


num_of_servobd=  4
servobd = [0]*num_of_servobd

num_of_modbody=  3
modbody = [0]*num_of_modbody
modybody = [0]*num_of_modbody
modxbody = [0]*num_of_modbody
jointx = [0]*num_of_modbody
jointy = [0]*num_of_modbody
propriceptivesenx = [0]*num_of_modbody
propriceptiveseny = [0]*num_of_modbody
raysenhead = [0]*num_of_modbody
raysentail = [0]*num_of_modbody

sim = pyrosim.Simulator(eval_time=1000, debug=True, play_paused= True, use_textures=True, xyz=[-25,-50,0])

# head
head=sim.send_box(x=-8.5/2, y=0, z=7.7/2, mass=5.0, r1=0, r2=0, r3=1, length=6.9, width=8.5, height=7.7, collision_group='robot', r=0, g=0, b=1) 
headj=sim.send_box(x=-10.35, y=-2.43, z=4.7, mass=1.0, r1=0, r2=0, r3=1, length=2.05, width=3.7, height=5, collision_group='robot', r=0, g=0, b=1) 
sim.send_fixed_joint(head, headj)
# tail
tail=sim.send_box(x=-80.75, y=0, z=7.7/2, mass=5.0, r1=0, r2=0, r3=1, length=6.9, width=12.5, height=7.7, collision_group='robot', r=0, g=.5, b=1)  
tailj=sim.send_box(x=-72.65, y=0, z=7.2, mass=1.0, r1=0, r2=0, r3=1, length=6, width=3.7, height=1, collision_group='robot', r=0, g=.5, b=1)  
sim.send_fixed_joint(tail, tailj)
# servobody
for i in range (num_of_servobd):
    servobd[i] = sim.send_box(x=-14.5-(18*i), y=0, z=4.67, mass=1.0, r1=0, r2=0, r3=1, length=2.8, width=10.2, height=4.2, collision_group='robot', r=.8, g=0, b=0)
# modbody
for i in range (num_of_modbody):
    modbody[i] = sim.send_box(x=-23.5-(18*i), y=0, z=4.67, mass=1.0, r1=0, r2=0, r3=1, length=6, width=6, height=6, collision_group='robot', r=0, g=.6, b=0)
    modxbody[i] = sim.send_box(x=-18.65-(18*i), y=0, z=7.2, mass=1.0, r1=0, r2=0, r3=1, length=5, width=3.7, height=1, collision_group='robot', r=0, g=.6, b=0)
    modybody[i] = sim.send_box(x=-28.35-(18*i), y=-2.2, z=4.67, mass=1.0, r1=0, r2=0, r3=1, length=1.6, width=3.7, height=5, collision_group='robot',  r=0, g=.6, b=0)
    #joints
    sim.send_fixed_joint(modbody[i], modxbody[i])
    sim.send_fixed_joint(modbody[i], modybody[i])
    jointx[i] = sim.send_hinge_joint(modxbody[i], servobd[i], x=-10.35, y=-1.68, z=4.63, n1=0, n2=0, n3=1, lo=(-math.pi / 4.0), hi=(math.pi / 4.0), speed=1.0, torque=30.0, position_control=True)
    jointy[i] = sim.send_hinge_joint(modybody[i], servobd[i+1], x=-30.2 - (18*i), y=-1.4, z=4.7, n1=0, n2=1, n3=0, lo=(-math.pi / 4.0), hi=(math.pi / 4.0), speed=1.0, torque=30.0, position_control=True)
    #propriceptivesensor
    propriceptivesenx[i] = sim.send_proprioceptive_sensor(jointx[i])
    propriceptiveseny[i] = sim.send_proprioceptive_sensor(jointy[i])

# joints
jointhead=sim.send_hinge_joint(headj, servobd[0], x=-10.35, y=-1.68, z=4.63, n1=0, n2=1, n3=0, lo=(-math.pi / 4.0), hi=(math.pi / 4.0), speed=1.0, torque=30.0, position_control=True)
jointtail=sim.send_hinge_joint(tailj, servobd[3], x=-72.65, y=0, z=7.2, n1=0, n2=0, n3=1, lo=(-math.pi / 4.0), hi=(math.pi / 4.0), speed=1.0, torque=30.0, position_control=True)
#sensor
propriceptivesenhead= sim.send_proprioceptive_sensor(jointhead)
propriceptivesentail= sim.send_proprioceptive_sensor(jointtail)
#raysensor
raysenhead[0]= sim.send_ray_sensor(body_id=0, x=0, y=0, z=0, r1=0, r2=0, r3=1, max_distance=10)
raysentail[0]= sim.send_ray_sensor(body_id=0, x=0, y=0, z=0, r1=0, r2=0, r3=1, max_distance=10)
raysenhead[1]= sim.send_ray_sensor(body_id=0, x=0, y=0, z=0, r1=0, r2=0, r3=1, max_distance=10)
raysentail[1]= sim.send_ray_sensor(body_id=0, x=0, y=0, z=0, r1=0, r2=0, r3=1, max_distance=10)
raysenhead[2]= sim.send_ray_sensor(body_id=0, x=0, y=0, z=0, r1=0, r2=0, r3=1, max_distance=10)
raysentail[2]= sim.send_ray_sensor(body_id=0, x=0, y=0, z=0, r1=0, r2=0, r3=1, max_distance=10)
    
    
sim.start()
sim.wait_to_finish()