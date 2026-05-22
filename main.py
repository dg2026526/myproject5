
Web VPython 3.2

b = box(size = vec(192,101,2)) 
b = box(size = vec(192,15,0.5),pos = vec(0,-44,1),color = color.blue)
b = box(size = vec(1,101,0.5),pos = vec(-96,0,1),color = color.blue)
b = box(size = vec(1,101,0.5),pos = vec(96,0,1),color = color.blue)
b = box(size = vec(192,7,2), pos = vec(0,54,0), color = color.blue)
b = box (size = vec(5.5,0.5,2), pos = vec (76,51.7,0.3),color = color.blue)

b = box (size = vec(0.5,5.5,2), pos = vec (81.5,54,0.3),color = color.blue)
b = box (size = vec(5.5,0.5,2), pos = vec (84,51.6,0.3),color = color.blue)
b = box (size = vec(5.5,0.5,2), pos = vec (84,56,0.3),color = color.blue)
b = box (size = vec(5.5,0.5,2), pos = vec (76,51.6,0.3),color = color.blue)

b = box (size = vec(6,6,2), pos = vec (92,54,0.2))
b = box (size = vec(6,6,2),  pos = vec (84,54,0.2))        
b = box (size = vec(6,6,2), pos = vec (76,54,0.2))    
b = box(color =  color.black ,make_trail = True, pos = vec(0,0,1))


  

xx = 90
yy = -53
cube0=box(size=vec(4,4,1.4),pos=vec(0+xx,0+yy,2),opacity=1,color=color.red)
cube1=box(size=vec(4,4,1.4),pos=vec(3+xx,0+yy,2),opacity=1,color=color.yellow)
cube2=box(size=vec(4,4,1.4),pos=vec(6+xx,0+yy,2),opacity=1,color=color.blue)
cube3=box(size=vec(4,4,1.4),pos=vec(9+xx,0+yy,2),opacity=1,color=color.white)
cube4=box(size=vec(4,4,1.4),pos=vec(12+xx,0+yy,2),opacity=1,color=color.black)

while True:
    rate(100)
    if scene.mouse.pick==cube0:
        b.color=color.red
        b.trail_color=color.red
        cube1.color=color.red
        cube2.color=color.red
        cube3.color=color.red
        cube4.color=color.red
    if scene.mouse.pick==cube1:
        b.color=color.blue
        b.trail_color=color.blue
        cube1.color=color.blue
        cube2.color=color.blue
        cube3.color=color.blue
        cube4.color=color.blue
    if scene.mouse.pick==cube2:
        b.color=color.yellow
        b.trail_color=color.yellow
        cube1.color=color.yellow
        cube2.color=color.yellow
        cube3.color=color.yellow
        cube4.color=color.yellow
    if scene.mouse.pick==cube3:
        b.color=color.white
        b.trail_color=color.white
        cube0.color=color.white
        cube1.color=color.white
        cube2.color=color.white
        cube3.color=color.white
        cube4.color=color.white
    if scene.mouse.pick==cube4:
        b.color=color.black
        b.trail_color=color.black
        cube0.color=color.black
        cube1.color=color.black
        cube2.color=color.black
        cube3.color=color.black
        cube4.color=color.black


    k = keysdown()
    if 'd' in k :
        b.pos.x = b.pos.x +0.1  
    if 'a' in k :
        b.pos.x = b.pos.x -0.1  
    if 'w' in k :
        b.pos.y =b.pos.y + 0.1
    if 's' in k:
        b.pos.y =b.pos.y -0.1
