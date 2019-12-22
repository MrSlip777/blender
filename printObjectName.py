#summary
#change object name

import bpy

obj_s = bpy.data.objects
i = int(0)

for obj in obj_s:
    obj.name = "AAAA" + str(i)
    i+=1