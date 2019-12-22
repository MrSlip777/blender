#summary
#setting weight zero

import bpy

obj_s = bpy.data.objects

for obj in obj_s:
    if obj.name == "USBCable1":
        vg_s = obj.vertex_groups
        break

for v in obj.data.vertices:
    for vge in v.groups:
        #bpy.context.object.active_index = vge.group
        if vge.group != 100:
            vge.weight = 0.0

