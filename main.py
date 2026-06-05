<수행평가 최종본>
Web VPython 3.2

b = box(size = vec(192,101,2)) 
b = box(size = vec(192,15,0.5),pos = vec(0,-44,1),color = color.blue)
b = box(size = vec(1,101,0.5),pos = vec(-96,0,1),color = color.blue)
b = box(size = vec(1,101,0.5),pos = vec(96,0,1),color = color.blue)
b = box(size = vec(192,7,2), pos = vec(0,54,0), color = color.blue)
b = box (size = vec(6,6,2), pos = vec (92,54,0.2),texture = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQOLNEc_KuJVkSe4EEiqqv-nbYSQjA8PIHolQ&s") 
b = box (size = vec(6,6,2),  pos = vec (84,54,0.2))        
b = box (size = vec(6,6,2), pos = vec (76,54,0.2))
b = box (size = vec(6,6,2), pos = vec (76,54,0.2))
b = box(color =  color.black ,make_trail = True, pos = vec(0,0,1))
 

xx = 90
yy = -53
cube0=box(size=vec(4,4,1.4),pos=vec(25-xx,0+yy,2),opacity=1,color=color.red)
cube1=box(size=vec(4,4,1.4),pos=vec(20-xx,0+yy,2),opacity=1,color=color.yellow)
cube2=box(size=vec(4,4,1.4),pos=vec(15-xx,0+yy,2),opacity=1,color=color.blue)
cube3=box(size=vec(4,4,1.4),pos=vec(10-xx,0+yy,2),opacity=1,color=color.white)
cube4=box(size=vec(4,4,1.4),pos=vec(5-xx,0+yy,2),opacity=1,color=color.black)

cubes = [cube0,cube1,cube2,cube3,cube4]

while True:
    rate(100)
    if scene.mouse.pick==cube0:
        b.color=color.red
        b.trail_color=color.red
        for cube in cubes : 
            cube.color=color.red
    if scene.mouse.pick==cube1:
        b.color=color.blue
        b.trail_color=color.blue
        for cube in cubes : 
            cube.color=color.blue
    if scene.mouse.pick==cube2:
        b.color=color.yellow
        b.trail_color=color.yellow
        for cube in cubes : 
            cube.color=color.yellow
    if scene.mouse.pick==cube3:
        b.color=color.white
        b.trail_color=color.white
        for cube in cubes : 
            cube.color=color.white
    if scene.mouse.pick==cube4:
        b.color=color.black
        b.trail_color=color.black
        for cube in cubes : 
            cube.color=color.black

    k = keysdown()
    if 'd' in k :
        b.pos.x = b.pos.x +0.1  
    if 'a' in k :
        b.pos.x = b.pos.x -0.1  
    if 'w' in k :
        b.pos.y =b.pos.y + 0.1
    if 's' in k:
        b.pos.y =b.pos.y -0.1
